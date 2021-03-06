# Floræcite
Species Memory Assistance (Flora + recite)：species identification and correcting the common names and Latin names spelling.
![gui](images/gui.png)
## How to use it

### 1. Preparation
**Download** by clicking **release**, or this url: https://github.com/HowcanoeWang/Floraecite/releases

Download the <a href="https://github.com/HowcanoeWang/Floraecite/releases/download/v1.0.1/Floraecite_v1.0.1.exe">Floraecite_v1.0.1.exe</a> and <a href="https://github.com/HowcanoeWang/Floraecite/releases/download/v1.0.1/Data4Example.zip">Data4Example.zip</a>


#### 1.1 Use course provided database
There is only a few example pictures in the **Data4Example.zip** Folder. For all FOR/ENR2425 courses image data, click here: <a href="https://github.com/HowcanoeWang/Floraecite/releases/download/v1.0/UNB2425Pictures161204.zip">**UNB extra pictures**</a> (200 Common species in Eastern North America)

> The Extra Image Data (000.xlsx and 200 pictures) are examples provided by the course of ***Autecology(FOR2425), College of Foresty and Geology，University of New Brunswick***

#### 1.2 Make your own database
* The 000.xlsx is the default indexing file that you should not change the name (`000.xlsx`) of this file.
* This program could only read sheet1 in the Excel. Please do not add information to other sheets.
* The data structure of 000.xlsx is:

    | (Picture filename) | (Latin name) | (Common name) | (Latin required) |
    |------------------|------------|-------------|----------------|
    | 001 | Polystichum acrostichoides | Christmas fern | 0 |
    | 002 | Pteridium aquilinum | bracken fern | 1 |

    Where: 
    
    0 == Latin names don't need to recite, 1 == Latin Name required.   
    If you just want to identify plants rather than remembering their Latin names, just put zeros in that column.
    
    The first row should **NOT** be put into the sheet(just tell you the meaning of each column), please start with your picture names in the first line directly. Here is the example:
    ![xlsx example](images/xlsx.png)
    
    Picture names in the sheet (Column A) **must the same as** picture names in the Data folder. 
    
    Other languages which are included in UTF-8 format are supported.
    
    Recommend picture format of **.jpg**, support format of **.png** and **.gif**
    
    **Please make sure all the picture files in the same format.**

### 2. Common Using
> After opening the programme, it will create a log file called memeory.floraecite in the picture data folder, this ensure the programme could list your least familiar species at the first beginning with your using process. Please **DO NOT** delete it!

#### 2.1 Viewing mode (Default)
Click next to view the species pictures and their names
![view](images/view.gif)

#### 2.2 Testing mode
Click `Testing mode` to switch to this mode, all the name will change to blank for typing.
Click `Next` to submit current answer, it will tell you correct or not. If correct, go to next species, if not, the `Help` button will enabled to give correct answer
![view](images/test.gif)


## Troubleshoot
1. OS Version conflict  
    * **[Error]**   
        This verison of this file is not compatible with the version of Windows you're running. Check your computer's system information to see whether you need an x86 (32-bit) or x64 (64-bit) verion of the program.  
        【此文件的版本与正在运行的WINDOWS版本不兼容，请检查计算机的系统信息以了解需要X86位（32位）还是X64】
    * **[Fix]**  
        Download Floraecite version that newer than v1.0.1  
1. DLL missing
    * **[Error1]**  
        The program can’t start because MSVCR100.dll is missing from your computer  
        【无法启动此程序，因为计算机中丢失MSVCR100.dll。尝试重新安装该程序以解决此问题】
    * **[Fix]**  
        What hides behind this name is the Microsoft Visual C++ Redistributable which can easily be downloaded on the Microsoft website as x86 or x64 edition:

        32bit：http://www.microsoft.com/download/en/details.aspx?id=5555

        64bit：http://www.microsoft.com/download/en/details.aspx?id=14632

        Usually the application that misses the dll indicates what version you need - if one does not work, simply install the other.
    * **[Error2]**  
        The program can't start because api-ms-win-crt-runtime-l1-1.0.dll is missing from your computer. Try reinstalling the program to fix this problem  
        【无法启动此程序，因为计算机中丢失api-ms-win-crt-runtime-|1-1-0.dll尝试重新安装该程序以解决此问题】
    * **[Fix]**  
        1. Install all pending Windows Updates
            Go to Start – Control Panel – Windows Update
            Check for updates and install all pending updates, then restart the computer.
            After the restart repeat the steps above again until no more updates are available.
        
        2. Download the Visual C++ Redistributable 2015
            *Visual C++ Redistributable 2008 and 2010 are needed for installing the 2015 if your computer doesn't have*
            
            *After downloading, please DO NOT just double click to run, RIGHT click and using administrator rights to run*
            
            32bit: http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x86.exe
            
            64bit: http://download.microsoft.com/download/9/3/F/93FCF1E7-E6A4-478B-96E7-D4B285925B00/vc_redist.x64.exe
        
        3. Run the vcredist_x64.exe (64-bit) or vcredist_x86.exe (32-bit) and select ***Uninstall if already installed***
        
        4. Restart the computer and run the Floraecite again.

### Help Us
If you meet any other bug, please contact the author without hesitation. You could e-mail the author or make comments on Github. Describe the problem and your operation process in detail.

--- 

## Update log
### 16.11.27
#### Beta1.7.1
+ add new version download wait string

### 16.11.26
#### Beta1.7.0
+ fix small bugs
+ change names in 000.xlsx file from ’ to '

### 16.11.23
#### Beta1.6.9
+ pack pictures into zip files
+ add new version detection function
+ fix rename picture can not change log bug

### 16.11.22
#### Beta1.6.8
+ add picture data choose function
+ display Mastery in the GUI
### 16.11.21
+ Add 13 Lichens and Bryophytes pictures
+ Moderate 000.xlsx
+ change file positions
#### Beta 1.6.7    
1. fix picture list bugs
2. change folder structure

### 16.11.20
#### Beta1.6.6
+ Improve mastary calculation

#### Beta1.6.5
+ Add icon

#### Beta1.6.4
+ Fix Next button can not rebound

### 16.11.19
#### Beta1.6.3
##### Add
+ Checking before operating the program
+ \<Enter> to 'next' instead Of clicking Button    

##### Debug 
+ Fix user delete pictures in the folder that caused program broken up    

#### Beta1.6.1

##### New: 
+ Activate Mastary rank methods 

##### Debug: 
+ Fix small screen can not show the GUI 
+ Fix log file read error 

#### Beta1.5.0
+ main functions, including veiwing and testing mode, help, and Mastery recording

### 16.11.18
+ Add version auther and official url link
+ Add single select button, excel data reading, picture list acquire

### 16.11.17
+ coding

### 16.11.15
+ github use learning

### 16.10.31
+ Program started
