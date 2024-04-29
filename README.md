# FaucetEarner auto claim

> [!NOTE]
> Tested on Windows, Linux and Android

## Windows
> You can also install Python 3 on your OS and clone this repo.
> But the easiest way is to follow these steps.

1. Download the tool [here](https://drive.google.com/file/d/1OKRopW3QBpdE2qSEmGFUrPa-69kTU1Ca/view?usp=sharing)

2. Exctract the directory

3. Enter into the exctracted directory

4. Edit environment file
	- Fill all fields
	```
	USER=<username>
	MAIL=<email>
	PASSWORD=<password
	```

    - Save the file.

5. Execute `Faucetearner.exe` to run tool

6. Stop tool by hiting `CTRL + C`

## Linux
> You should have Python 3 on your environment

1. Clone this repo
   ```
   git clone https://github.com/dijey099/auto-claim-faucetearner.git
   ```

2. Enter to the tool's directory
	```
	cd auto-claim-faucetearner
	```

3. Install dependancies
	```
	pip install -r requirements.txt
	```

4. Edit environment file
	- Open `.env` in nano text editor
	```
	nano .env
	```

	- Edit these lines
	```
	USER=<username>
	MAIL=<email>
	PASSWORD=<password
	```

	- Close nano by clicking on `CTRL` and then `X`, hit `Y` for Yes to save file, keep the name `.env` and hit **Enter**

5. Run tool
   ```
   python faucetearner.py
   ```



## Android
### First time you use the tool
> Follow these steps if it's your first time to use the tool.
> Dependancies should be installed once.

1. Dowload Termux from F-Droid [here](https://f-droid.org/repo/com.termux_118.apk) (if you already installed it using PlayStore, then uninstall)

2. Install the downloaded APK file and launch it

3. Setup Termux storage
   ```
   termux-setup-storage
   ```

4. Close and force exit Termux

5. Reopen Termux

6. Update and Upgrade some package
   ```
   yes | pkg update -y && yes | pkg upgrade -y
   ```

7. Install pip
   ```
   yes | pkg install python-pip -y
   ```

8. Install Git
   ```
   pkg install git
   ```

9. Clone this repo
   ```
   git clone https://github.com/dijey099/auto-claim-faucetearner.git
   ```

10. Enter to the tool's directory
	```
	cd auto-claim-faucetearner
	```

11. Install dependancies
	```
	pip install -r requirements.txt
	```

12. Install driver
	```
	yes | pkg install x11-repo -y
	yes | pkg install firefox -y
	yes | pkg install geckodriver -y
	```

13. Edit environment file
	- Open `.env` in nano text editor
	```
	nano .env
	```

	- Edit these lines
	```
	USER=<username>
	MAIL=<email>
	PASSWORD=<password
	```

	- Close nano by clicking on `CTRL` and then `X`, hit `Y` for Yes to save file, keep the name `.env` and hit **Enter**

13. Run tool
	```
	python faucetearner.py
	```

14. Stop tool by hiting `CTRL` and then `C`

### Next time you use the tool
1. Open Termux

2. Enter to tool's directory
   ```
   cd auto-claim-faucetearner
   ```

3. Run tool
   ```
   python faucetearner.py
   ```

4. Stop tool by hiting `CTRL` and then `C`