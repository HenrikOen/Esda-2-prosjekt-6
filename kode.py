import numpy as np
import matplotlib.pyplot as plt
import csv
import os



#Definin the file paths:
Oscilliscope_open_lokke     = "Esda-2-prosjekt-6\\Malinger\\Oscilliscope_open_lokke.csv"
Osilliscope_100Kohm         = "Esda-2-prosjekt-6\\Malinger\\Osilliscope_100Kohm.csv"
Osilliscope_100ohm          = "Esda-2-prosjekt-6\\Malinger\\Osilliscope_100ohm.csv"

tenx_open_lokke             = "Esda-2-prosjekt-6\\Malinger\\10x_open_lokke.csv"
tenx_100kohm                = "Esda-2-prosjekt-6\\Malinger\\10x_100kohm.csv"
tenx_100ohm                 = "Esda-2-prosjekt-6\\Malinger\\10x_100ohm.csv"





#Function for converting file to lists (oscilliscope):
def file_to_list(file, time_coloumn, Voltage1_column, Voltage2_column):
    Voltage1_list =[]
    Voltage2_list =[]
    time_list     = []
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            time_list.append(float(row[time_coloumn]))
            Voltage1_list.append(float(row[Voltage1_column]))
            Voltage2_list.append(float(row[Voltage2_column]))

    return  time_list, Voltage1_list, Voltage2_list


#Defining function to convert csv file to lists (Amplitude response):
def file_to_list_Response(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):
                continue
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
        return freq_list, magnetude_list



Oscilliscope_open_lokke_t, Oscilliscope_open_lokke_V1, Oscilliscope_open_lokke_V2   = file_to_list(Oscilliscope_open_lokke, 0, 1, 2)
Osilliscope_100Kohm_t, Osilliscope_100Kohm_V1, Osilliscope_100Kohm_V2               = file_to_list(Osilliscope_100Kohm, 0, 1, 2)
Osilliscope_100ohm_t, Osilliscope_100ohm_V1, Osilliscope_100ohm_V2                  = file_to_list(Osilliscope_100ohm, 0, 1, 2)

tenx_open_lokke_t, tenx_open_lokke_V1, tenx_open_lokke_V2                           = file_to_list(tenx_open_lokke, 0, 1, 2)
tenx_100kohm_t, tenx_100kohm_V1, tenx_100kohm_V2                                    = file_to_list(tenx_100kohm, 0, 1, 2)
tenx_100ohm_t, tenx_100ohm_V1, tenx_100ohm_V2                                       = file_to_list(tenx_100ohm, 0, 1, 2)





#creating folder for graphs:
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)

#Plottign and saving graphs:

#Oscilliscope, open loop:

fig, ax1 = plt.subplots()
plt.grid()
ax1.tick_params(axis='y', labelcolor='b')
plt.plot(np.array(Oscilliscope_open_lokke_t)*1000, Oscilliscope_open_lokke_V1)
ax1.set_xlabel('Time [ms]')
ax1.set_ylabel('$v_2$ [V]', color='b')
ax1.tick_params(axis='y', labelcolor='b')
plt.legend(['$v_2$'])

ax2 = ax1.twinx()  
plt.plot(np.array(Oscilliscope_open_lokke_t)*1000, np.array(Oscilliscope_open_lokke_V2)*1000, color='red')
ax2.set_ylabel('$v_1$ [mV]', color='r')
ax2.tick_params(axis='y', labelcolor='r')

ax2.set_ylim(-100, 100)
plt.title('Input and output signal, open loop')
plt.xlabel('Time [ms]')
plt.legend(['$v_1$'])
plt.tight_layout()
plt.savefig('Graphs\Oscilliscope_open_lokke.png', dpi=300)




#Oscilliscope, R=100kOhm:

fig, ax1 = plt.subplots()
plt.grid()

ax1.tick_params(axis='y', labelcolor='b')
plt.plot(np.array(Osilliscope_100Kohm_t)*1000, Osilliscope_100Kohm_V1)
ax1.set_xlabel('Time [ms]')
ax1.set_ylabel('$v_2$ [V]', color='b')
ax1.tick_params(axis='y', labelcolor='b')
plt.legend(['$v_2$'])

ax2 = ax1.twinx()  
plt.plot(np.array(Osilliscope_100Kohm_t)*1000, np.array(Osilliscope_100Kohm_V2)*1000, color='red')
ax2.set_ylabel('$v_1$ [mV]', color='r')
ax2.tick_params(axis='y', labelcolor='r')

ax2.set_ylim(-100, 100)
plt.title('Input and output signal, R = 100k$\Omega$')
plt.xlabel('Time [ms]')
plt.legend(['$v_1$'])

plt.tight_layout()
plt.savefig('Graphs\Osilliscope_100Kohm.png', dpi=300)



#Oscilliscope, R=100Ohm:
fig, ax1 = plt.subplots()
plt.grid()

ax1.tick_params(axis='y', labelcolor='b')
plt.plot(np.array(Osilliscope_100ohm_t)*1000, Osilliscope_100ohm_V1)
ax1.set_xlabel('Time [ms]')
ax1.set_ylabel('$v_2$ [V]', color='b')
ax1.tick_params(axis='y', labelcolor='b')
plt.legend(['$v_2$'])

ax2 = ax1.twinx()  
plt.plot(np.array(Osilliscope_100ohm_t)*1000, np.array(Osilliscope_100ohm_V2)*1000, color='red')
ax2.set_ylabel('$v_1$ [mV]', color='r')
ax2.tick_params(axis='y', labelcolor='r')

ax2.set_ylim(-100, 100)
plt.title('Input and output signal, R = 100$\Omega$')
plt.xlabel('Time [ms]')
plt.legend(['$v_1$'])

plt.tight_layout()
plt.savefig('Graphs\Osilliscope_100ohm.png', dpi=300)




#Oscilliscope, -10xAmplification

#  open loop:
plt.figure()
plt.plot(np.array(tenx_open_lokke_t)*1000, np.array(tenx_open_lokke_V1)*1000)
plt.plot(np.array(tenx_open_lokke_t)*1000, np.array(tenx_open_lokke_V2)*1000)
plt.title('Input and output signal, -10x amplification, open loop')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude [mV]')
plt.legend(['$v_1$', '$v_2$'])
plt.grid()
plt.savefig('Graphs\ tenx_open_lokke.png')


#Oscilliscope, -10xAmplification R=100kOhm:
plt.figure()
plt.plot(np.array(tenx_100kohm_t)*1000, np.array(tenx_100kohm_V1)*1000)
plt.plot(np.array(tenx_100kohm_t)*1000, np.array(tenx_100kohm_V2)*1000)
plt.title('Input and output signal, -10x amplification, $R_{L_1}=100k\Omega$')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude [mV]')
plt.legend(['$v_1$', '$v_2$'])
plt.grid()
plt.savefig('Graphs\ tenx_R=100kohm.png')


#Oscilliscope, -10xAmplification R=100Ohm:
plt.figure()
plt.plot(np.array(tenx_100ohm_t)*1000, np.array(tenx_100ohm_V1)*1000)
plt.plot(np.array(tenx_100ohm_t)*1000, np.array(tenx_100ohm_V2)*1000)
plt.title('Input and output signal, -10x amplification, $R_{L_1}=100\Omega$')
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude [mV]')
plt.legend(['$v_1$', '$v_2$'])
plt.grid()
plt.savefig('Graphs\ tenx_R=100ohm.png')

# plt.show()


