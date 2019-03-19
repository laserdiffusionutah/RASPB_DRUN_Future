#! /usr/bin/python3
"""
Created on Wed Jan 16 14:46:37 2019

@author: Tim
"""
import time 
from scipy import misc
from laser_diffusion_alpha import region_analyzer,rank_round,reorder,\
     transform_image,filter_rgb_weight,Image_norm,diffuse_fit,fix_skewed
import datetime


t0import = open('./timeset.txt')
t0 =float(t0import.read())
t0import.close()
tf = time.time()
t_actual = tf-t0
I = misc.imread('./laser_image.jpg')
pts = 4
e,middle = region_analyzer(I,pts,maxitter=100)    
e_round, middle_round = rank_round(e,middle,pts) 
transform = reorder(middle_round,pts)
#    transform_image(I,transform)
#        ###THis portion of the code orders the points for transform image
Im  = transform_image(I,transform)
I_av = filter_rgb_weight(Im,a=10,b=1,c=10)
y,x = Image_norm(I_av,pixel_num=2,area=300)
xplot,yplot = fix_skewed(x,y)
D_2,D_2u,C1,C2,C3 = diffuse_fit(xplot,yplot,t_actual,0)
line = "\n"
export_name = str(datetime.date.today())+'_Diffusion_Data_set.txt'
enexport = open(export_name,'a')
enexport.write(line+str(t_actual)+' '+str(D_2))
enexport.close()
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
plt.plot(xplot,yplot,'ok')
