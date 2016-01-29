# DirBrute  
多线程WEB目录爆破工具(含字典)  
  
```
Usage: dirbrute.py target [options] 
Example: python dirbrute.py www.cdxy.me -e php -t 10
         python dirbrute.py www.cdxy.me -t 10 -d ./dics/ASP/uniq

Options:
  -h, --help            show this help message and exit
  -e EXT, --ext=EXT     Choose the extension: php asp aspx jsp...
  -t THREADS_NUM, --threads=THREADS_NUM
                        Number of threads. default = 10
  -d DIC_PATH, --dic=DIC_PATH
                        Default dictionaty: ./dics/dirs.txt
```  

# 计算  
 - 多线程并行  
 - 非阻塞  
  
# 附加模块  
 - WAF探测  
  
```
checking if the target is protected by 
some kind of WAF/IPS/IDS

heuristics detected that the target 
is protected by some kind of WAF/IPS/IDS

are you sure that you want to 
continue with further fuzzing? [y/N]
```  

# 字典  
附加收集各类型字典未删减版    
 - ASP
 - JSP
 - PHP
 - COMMON 通用路径
 - DB 数据库文件
 - CMS_EXP CMS探测向量和一些常见漏洞利用点
 - %EXT% 猪猪侠大牛的字典,需要指定后缀名使用
