#!/usr/bin/env python3
"""
[+] Sql injections Scanner [+]

_< Find Sql`s sites >_

DEV#Host1let => R3D\|/R00m


License :

Copyright (c) 2023 R3D\|/R00m Host1let: sqlFinder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pystyle
import sys 
import googlesearch

lis = sys.argv

class sqlFinder:
    
    def __init__(self, query: str = "inurl", phpDork: str = "*.php?id=", siteDomain: str = "in", lang: str = "en", resultNumber: int = 10) -> None:
        self.q = query
        self.pd = phpDork
        self.sd = siteDomain
        self.l = lang
        self.rn = resultNumber
        
    def start(self):
        self.all_ = f"{self.q}:{self.pd} site:{self.sd}"
        
        for results in googlesearch.search(self.all_, self.rn, self.l):
            pystyle.Write.Print(results, pystyle.Colors.purple_to_red, 0)


class Session:
    
    def Client():
        
        if "-q" in lis:
            qu = lis[lis.index('-q')+1]
            
            if "-d" in lis:
                dork = lis[lis.index('-d')+1]
                
                if "-D" in lis:
                    domain = lis[lis.index('-D')+1]
                    
                    if "-r" in lis:
                        resNumber = int(lis[lis.index('-r')+1])
                        
                        sqlFinder(qu, dork, domain, resultNumber=resNumber).start()
                        
                    else:
                        sqlFinder(qu, dork, domain).start()
                        
                else:
                    sqlFinder(qu, dork).start()
                    
            else:
                sqlFinder(qu).start()
                
        if "--local" in lis:
            sqlFinder().start()
                
        if len(lis) == 1:
            pystyle.Write.Print('''Faild To use: [-h / --help] [-q: set query] [-d: set dork] [-D: set domain] [-r: result time]

Examples: 

sqlFinder.py -q inurl -d *.php.id?= -D ae -r 12

sqlFinder.py -q inurl -d *.php.id?= -D ae

sqlFinder.py -q inurl -d *.php.id?= 

sqlFinder.py -q inurl

and you can selected randomly

start with diffault values: sqlFinder.py --local''', pystyle.Colors.purple_to_red, 0.001)
            print()
            print()
            
        if "-h" in lis or "--help" in lis:
            pystyle.Write.Print('''Faild To use: [-h / --help] [-q: set query] [-d: set dork] [-D: set domain] [-r: result time]

Examples: 

sqlFinder.py -q inurl -d *.php.id?= -D ae -r 12

sqlFinder.py -q inurl -d *.php.id?= -D ae

sqlFinder.py -q inurl -d *.php.id?= 

sqlFinder.py -q inurl

and you can selected randomly
start with diffault values: sqlFinder.py --local''', pystyle.Colors.purple_to_red, 0.001)
            print()
            print()
            
Session.Client()