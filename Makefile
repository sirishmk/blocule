#Add wallet versions here
TRX_WALLET_HASH=afe22ccda5c4a137dd35da22f4f879f3f3786f26

#Wallet folder names
TRX_F=trx-wallet

all: mk_dirs wallets dep setup_wallets build_wallets

wallets: get_trx_wallet

#Get wallets
get_trx_wallet:
	git clone https://github.com/tronprotocol/wallet-cli $(TRX_F)
	cd $(TRX_F); git reset --hard $(TRX_WALLET_HASH)

#Get dependencies
dep:
	#Install protoc buf
	git clone https://github.com/google/protobuf.git ./tmp/protobuf
	cd ./tmp/protobuf; git submodule update --init --recursive; ./autogen.sh;./configure --prefix=/usr; make; make install
	sh -c 'echo /usr/lib >> /etc/ld.so.conf'
	ldconfig
	#Cleanup
	rm -rf ./tmp/protobuf

	#Get grpc-java
	git clone https://github.com/grpc/grpc-java.git ./deps/grpc-java
	patch ./deps/grpc-java/compiler/build.gradle < ./patches/grpc-java--build.gradle
	cd ./deps/grpc-java/compiler; CXXFLAGS="-I/usr/include" LDFLAGS="-L/usr/lib" ../gradlew java_pluginExecutable -Pprotoc=/usr/bin/protoc

	#get commons cli jar
	cd $(TRX_F); mkdir libs; cd libs; wget "http://central.maven.org/maven2/commons-cli/commons-cli/1.4/commons-cli-1.4.jar"
mk_dirs:
	mkdir deps
	mkdir tmp

setup_wallets:
	#TRX
	patch $(TRX_F)/build.gradle < ./patches/tron.build.gradle.patch
	cp -rf ./bloculeServer/emb $(TRX_F)/src/main/java/org/tron/

build_wallets:
	cd $(TRX_F); ./gradlew build



clean:
	rm -rf *~ \#* deps tmp $(TRX_F)
