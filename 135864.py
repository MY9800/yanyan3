
# coding: utf-8

# In[ ]:


# 查看当前挂载的数据集目录, 该目录下的变更重启环境后会自动还原
# View dataset directory. This directory will be recovered automatically after resetting environment. 
get_ipython().system('ls /home/aistudio/data')


# In[ ]:


# 查看工作区文件, 该目录下的变更将会持久保存. 请及时清理不必要的文件, 避免加载过慢.
# View personal work directory. All changes under this directory will be kept even after reset. Please clean unnecessary files in time to speed up environment loading.
get_ipython().system('ls /home/aistudio/work')


# 请点击[此处](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576)查看本环境基本用法.  <br>
# Please click [here ](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576) for more detailed instructions. 

# # 实验要求
# 
# 1.设计一个程序：接收10个人的工资数，计算每个人应纳个人所得税，以及个人所得税总额（拓展要求：计算或输入五险一金，扣除五险一金后计算其应纳个人所得税）； 
# 
# 2.设计一个程序：接收10个人的工资数，计算每个人需要的各种面值钞票的数量，以及各种面值钞票的总数。

# In[10]:


for num in range(10):
    gongzi = int(input("请输入工资数".format(num+1)))
    gongzi -= gongzi*0.08 + gongzi*0.02 + gongzi*0.004 + gongzi*0.12
    if gongzi <= 0:
        print('error')
    else:
        if gongzi <= 5000:
            print(0)
        elif gongzi <= 8000:
            print(gongzi*0.03)
        elif gongzi <= 17000:
            print(gongzi*0.1)
        elif gongzi <= 30000:
            print(gongzi*0.2)
        elif gongzi <= 40000:
            print(gongzi*0.25)
        elif gongzi <= 60000:
            print(gongzi*0.3)
        elif gongzi <= 85000:
            print(gongzi*0.35)
        else:
            print(gongzi*0.45)
    
    
    


# In[5]:


for num  in range(10):
    gongzi=int(input("请输入工资数"))
    if gongzi < 0:
        print('error')
    else:
        a=int(gongzi/100)
        b=int((gongzi-a*100)/50)
        c=int((gongzi-a*100-b*50)/20)
        d=int((gongzi-a*100-b*50-c*20)/10)
        e=int(gongzi-a*100-b*50-c*20-d*10)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

