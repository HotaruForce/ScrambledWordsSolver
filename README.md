# ScrambledWordsSolver
A simple python code to solve scrambled alphabets in word. 
Executable file included if you simply want to use it.
Use:
- ScrambledWordsSolver.exe is the program you want to use if you want to build exactly using every alphabets in the scrambled word.

  Download link: https://github.com/HotaruForce/ScrambledWordsSolver/raw/main/Dist/ScrambledWordsSolver.exe

- ScrambledWordsSolverExtra.exe is the program you want to use if you want to build exactly using every alphabets in the scrambled word and partially using existing alphabets given in the input.

  Download link: https://github.com/HotaruForce/ScrambledWordsSolver/raw/main/Dist/ScrambledWordsSolverExtra.exe

How to use:
Run main.py or extra.py.
Example:
input: "test"
expected output: 
- ScrambledWordsSolver.exe : 

  match word(s): 3
  
  ['sett', 'stet', 'test']
  
- ScrambledWordsSolverExtra.exe :

  match word(s): 15
  
  ['sett', 'stet', 'test', 'est', 'set', 'tst', 'es', 'et', 'se', 'st', 'te', 'ts', 'e', 's', 't']
  
  (Now, I know there is a single alphabet counted there but in the dictionary it is exist so I didn't changed it because it exists.)

Note:
You can change json file with any languange and it will be works.
Just make sure same format with english dictionary json file included in this code.

If someone find it useful and need any help to adapt it etc. just leave it in the issues. I just code this in the break time so forgive me if there is any mistake, flaw, or issues.

I just keep thinking to add classification of many alphabet used or any other feature but the basic task is already done for me so I will keep it short and simple except when I think it really needed.
