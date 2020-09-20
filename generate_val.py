import os
import pickle
pkls = [file for file in os.listdir('.') if file.endswith('pkl')]
count_num = 0
for i in pkls:
    count_num = count_num + 1
    print(count_num)
    line = []
    name = i.split('_')
    namenew = name[1]+'_'+name[2]+'/'+name[3]+'_'+name[4]+'/'+name[5][0:4]+'_pose.txt'
    file = open(i, 'rb')
    data = pickle.load(file)['gt_RTs']
    file.close()
    for num in range(1, data.shape[0]+1):
        line.append(str(num))
        line.append(str(data[num-1][0][0])+' '+str(data[num-1][0][1])+' '+str(data[num-1][0][2])+' '+str(1000*data[num-1][0][3]))
        line.append(str(data[num-1][1][0])+' '+str(data[num-1][1][1])+' '+str(data[num-1][1][2])+' '+str(1000*data[num-1][1][3]))
        line.append(str(data[num-1][2][0])+' '+str(data[num-1][2][1])+' '+str(data[num-1][2][2])+' '+str(1000*data[num-1][2][3]))
        line.append(str(data[num-1][3][0])+' '+str(data[num-1][3][1])+' '+str(data[num-1][3][2])+' '+str(data[num-1][3][3]))
    file = open(namenew, 'w')
    file.write('\n'.join(line))
    file.close()
