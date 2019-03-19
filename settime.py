# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:06:38 2019

@author: Tim
"""

import time
import datetime

t0 = time.time()

te = open('./timeset.txt','w')
te.write(str(t0))
te.close()

export_name = str(datetime.date.today())+'_Diffusion_Data_set.txt'
enexport = open(export_name,'w')
enexport.write('Time D')
enexport.close()
