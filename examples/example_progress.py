from compmake import comp, progress
import time

def mylongfunction():
    
    directories = ['a', 'b', 'c', 'd', 'e']
    n = len(directories)
    for i, dir in enumerate(directories):
        progress('Processing directories (first)', (i, n), 'Directory %s' % dir)
        
        N = 3
        for k in range(N):
            progress('Processing files (a)', (k, N), 'file #%d' % k)
            
            time.sleep( 1)
            
    for i, dir in enumerate(directories):
        progress('Processing directories (second)', (i, n), 'Directory %s' % dir)
    
        N = 3
        for k in range(N):
            progress('Processing files (b)', (k, N), 'file #%d' % k)
            
            time.sleep(  1)
            
            
comp(mylongfunction)
