import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from numpy.fft import fft 
import sounddevice as sd 

# Nom i cognoms: Kirian Rodríguez Alonso

#1. Reprodueix l'exemple fent servir diferents freqüències per la sinusoide. Al menys considera f_x = 4 kHz, 
# a banda d'una freqüència pròpia en el marge audible. Comenta els resultats.

T= 2.5                               
fm=8000                              
fx=4000                              
A=4                                 
pi=np.pi                             
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)      
sf.write('Kirian-so_exemple1.wav', x, fm)
Tx=1/fx                                   
Ls=int(fm*5*Tx)   

plt.figure(0)                            
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('Frequència = 4kHz. 5 periodes de la sinusoide')   
plt.show()   


# Analisis en freqüència
N=5000                      
X=fft(x[0 : Ls], N)           

# Representació del mòdul i la fase
k=np.arange(N)

plt.figure(1)                         
plt.subplot(211)                     
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                
plt.ylabel('$\phi_x[k]$')             
plt.show()   



# Ara amb una frequencia de 440Hz
T= 2.5                              
fm=8000                            
fx=440                              
A=4                               
pi=np.pi                            
L = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(L)                    
x = A * np.cos(2 * pi * fx * t)     
sf.write('Kirian-so_fitxer2.wav', x, fm)   
Tx=1/fx                                  
Ls=int(fm*5*Tx)                          

plt.figure(2)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                
plt.title('Frequència = 440Hz. 5 periodes de la sinusoide')   
plt.show()    

# Analisis en freqüència
N=5000                      
X=fft(x[0 : Ls], N)           

# Representació del mòdul i la fase

k=np.arange(N)                        
plt.figure(3)                         
plt.subplot(211)                     
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                
plt.ylabel('$\phi_x[k]$')             
plt.show()   

# 1r Cas
# En el cas del 4kHz podem veure que els 5 períodes duren 1ms amb una amplitud de 4.
# Podem observar que a més alta la freqüència, més aguda serà la senyal. 
# El numero de mostres es de 10, la transformada de la funció podem veure que es una sinc.
# La forma de la senyal es degut a que la frequencia de mostreig es aproximadament el doble de la frequencia de la sinusoide.

# 2n Cas
# En aquest segon cas(440Hz), hi ha 5 períodes de la sinusoide que duren 10ms i de amplitud 4. 
# El numero de mostres es de 90 en els 5 períodes. 
# La transformada ens mostra dos polsos amb un mòdul de 175.


# 2. Modifica el programa per considerar com a senyal a analitzar el senyal del fitxer wav que has creat (x_r, fm = sf.read('nom_fitxer.wav')).

#Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.

#Explica el resultat del apartat anterior.
x_r, fm = sf.read('Kirian-so_exemple1.wav')

Tm=1/fm                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

t=Tm* np.arange(len(x_r))               
sf.write('Kirian-so_ex2.wav', x_r, fm) 


#Representació 5 periodes
fx=fm/2
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(4)                             
plt.plot(t[0:Ls], x_r[0:Ls])                
plt.xlabel('t en segons')              
plt.title('Ex2, 5 periodes de la sinusoide')   
plt.show() 


#Reproducció del so
sd.play(x, fm)                

# Analisis en freqüència FFT
N=5000                      
X=fft(x[0 : Ls], N)           

# Representació del mòdul i la fase

k=np.arange(N)                        
plt.figure(5)                         
plt.subplot(211)                     
plt.plot(k,abs(X))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(X)))    
plt.xlabel('Index k')                
plt.ylabel('$\phi_x[k]$')             
plt.show()   

#Insereix a continuació una gràfica que mostri 5 períodes del senyal i la seva transformada.
#

#Explica el resultat del apartat anterior.
# Utilitzo el arxiu creat "Kirian-so_exemple1.wav" amb la freq de 4kHz,
# al utilitzar la mateixa frequència significa que obtindrem els mateixos resultats una altra vegada.


# 3. Modifica el programa per representar el mòdul de la Transformada de Fourier en dB i l'eix d'abscisses en el marge de 0 a fm/2 en Hz.
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=440                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('Kirian-so_ex3.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav
Tx=1/fx                                   
Ls=int(fm*Tx*5)                           

plt.figure(6)                             
plt.plot(t[0:Ls], x[0:Ls])               
plt.xlabel('t en segons')                 
plt.title('Ex3- 5 períodes')  
plt.show()   

#Reproducció del so
sd.play(x, fm)                

# Analisis en freqüència FFT
N=5000                      
X=fft(x[0 : Ls], N)           

# Representació del mòdul i la fase

k=np.arange(N)  
dBX = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N         #Calcul de la fk, pels valors de l'eix d'abscisses
plt.figure(7)
plt.subplot(211)   
plt.plot(fk,dBX[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')              
plt.show() 

#Comprova que la mesura de freqüència es correspon amb la freqüència de la sinusoide que has fet servir.
# Utilitzant la formula de fo=k/n * fm podem confirmar que es corresponen.

#Com pots identificar l'amplitud de la sinusoide a partir de la representació de la transformada? Comprova-ho amb el senyal generat.
#No es calculable, ja que al normalitzar-lo, amb el valor màxim obtenim de resultat 1.

# 4.ria un fitxer d'àudio en format wav i mono (el pots aconseguir si en tens amb altres formats amb el programa Audacity). Llegeix el fitxer d'àudio i comprova:


T= 0.025                               
data, fm =sf.read('luzbel44.wav')       
L = int(fm * T)                     
Tm=1/fm                            
t=Tm*np.arange(L)                 
print('Fm:',fm) #44100Hz
print('Numero de mostres:',L) #1102 mostres

sf.write('Kirian-so_ex4.wav', data, fm)

#Gràfica
plt.figure(8)                          
plt.plot(t[0:L],data[0:L])              
plt.xlabel('t(s)')               
plt.title('Ex. 4')  
plt.show() 

# Analisis en freqüència FFT
N=5000                      
X=fft(x[0 : L], N)           

# Representació del mòdul i la fase
k=np.arange(N)                                         
plt.figure(9)                         
dBX = 20*np.log10(np.abs(X)/max(np.abs(X)))
fk = k[0:N//2+1]*fm/N
plt.subplot(211)   
plt.plot(fk,dBX[0:N//2+1])  # Representació del mòdul de la transformada en dB y de 0 a FK/2
plt.title(f'Transformada del senyal de Ls={L} mostres amb DFT de N={N}')   
plt.ylabel('Mòdul en dB')                   
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])) )   
plt.xlabel('f en Hz')                
plt.ylabel('$\phi_x[k]$')          
plt.show() 
#- Quines son les freqüències més importants del segment triat?
# En l'arxiu de luzbel44.wav les freqüències més importants serien de 0Hz fins aproximadament uns 2kHz.