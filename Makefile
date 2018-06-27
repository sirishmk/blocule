run: run_trx_wallet run_disp

run_disp:
	python3 mainDisplay.py

run_trx_wallet:
	java -jar /home/pi/wallet-cli/build/libs/wallet-1.0-SNAPSHOT.jar
clean:
	rm -rf *~ \#* __pycache__
