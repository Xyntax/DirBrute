# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'
import libs.requests as requests
import sys
from libs.output import *

"""


IDS_WAF check payload from SQLMAP

IDS_WAF_CHECK_PAYLOAD = "AND 1=1 UNION ALL SELECT 1,2,3,table_name FROM information_schema.tables WHERE 2>1-- ../../../etc/passwd"

# Vectors used for provoking specific WAF/IDS/IPS behavior(s)
WAF_ATTACK_VECTORS = (
    "",  # NIL
    "search=<script>alert(1)</script>",
    "file=../../../../etc/passwd",
    "q=<invalid>foobar",
    "id=1 %s" % IDS_WAF_CHECK_PAYLOAD
)

IDS_WAF_CHECK_TIMEOUT = 10

"""


def checkWaf(url, header="", proxy="", timeout=5, allow_redirects=False):
    payload = '/cdxy.old/.svn/.bashrc/.mdb/.inc/etc/passwd'
    retVal = False
    retVal1 = False
    infoMsg = "checking if the target is protected by \n"
    infoMsg += "some kind of WAF/IPS/IDS\n"
    CLIOutput().printInfo(infoMsg)

    try:
        code = requests.get(url, stream=True, headers=header, timeout=timeout,
                            proxies=proxy,
                            allow_redirects=allow_redirects).status_code
        if code != 200:
            retVal = True
    except Exception, e:
        print e
        retVal = True

    try:
        code1 = requests.get(url + payload, stream=True, headers=header, timeout=timeout,
                             proxies=proxy,
                             allow_redirects=allow_redirects).status_code
        if code1 != 404:
            retVal1 = True
    except Exception, e:
        print e
        retVal1 = True

    if retVal:
        warnMsg = 'Target URL not stable\n'
        warnMsg += '[' + str(code) + '] ' + url + '\n'
        CLIOutput().printWarning(warnMsg)

        message = "are you sure that you want to \n"
        message += "continue with further fuzzing? [y/N] \n"
        CLIOutput().printNewLine(message)
        output = raw_input()
        if not output or output[0] not in ("Y", "y"):
            print 'User Quit!'
            sys.exit(0)

    if retVal1:
        warnMsg = "heuristics detected that the target \n"
        warnMsg += "is protected by some kind of WAF/IPS/IDS\n"
        CLIOutput().printWarning(warnMsg)

        message = "are you sure that you want to \n"
        message += "continue with further fuzzing? [y/N] \n"
        CLIOutput().printNewLine(message)
        output = raw_input()

        if not output or output[0] not in ("Y", "y"):
            print 'User Quit!'
            sys.exit(0)
