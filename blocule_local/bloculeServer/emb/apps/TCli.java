package org.tron.emb.apps;


import com.beust.jcommander.JCommander;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.tron.api.GrpcAPI.*;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import org.tron.common.utils.ByteArray;
import org.tron.common.utils.Utils;
import org.tron.protos.Contract.AssetIssueContract;
import org.tron.protos.Protocol.Account;
import org.tron.protos.Protocol.Block;
import org.tron.protos.Protocol.Transaction;
import org.tron.walletserver.WalletClient;
import org.tron.walletcli.Client;

import java.sql.Timestamp;
import java.util.*;
import java.util.Base64.Decoder;
import java.util.Base64.Encoder;


public class TCli {

    //private final long Balance;
    
    private static final Logger logger = LoggerFactory.getLogger("TCli");
    private Client client = new Client();

    
    private void login(String[] parameters) {
	if (parameters == null || parameters.length != 1) {
	    System.out.println("Login need 1 parameter like following: ");
	    System.out.println("Login Password ");
	    return;
	}
	String password = parameters[0];
	
	boolean result = client.login(password);
	if (result) {
	    logger.info("Login successful !!!");
	} else {
	    logger.info("Login failed !!!");
	}
    }
    
    private long getBalanceCli(String[] parameters) {
	String [] password = {parameters[0]};      
	this.login(password);
	
	Account account = client.queryAccount();
	if (account == null) {
	    logger.info("Get Balance failed !!!!");
	    return(-1);
	    
	} else {
	    long balance = account.getBalance();
	    logger.info("Balance = " + balance);
	    return(balance);
	}
    }

    private long sendCoinCli(String[] parameters) {
	if (parameters == null || parameters.length != 3) {
	    System.out.println("SendCoin need 3 parameter like following: ");
	    System.out.println("SendCoin Password ToAddress Amount");
	    return(0);
	}
	String password = parameters[0];
	String toAddress = parameters[1];
	String amountStr = parameters[2];
	long amount = new Long(amountStr);

	//Login before sending
	this.login(new String [] {password});
	
	boolean result = client.sendCoin(password, toAddress, amount);
	if (result) {
	    logger.info("Send " + amount + " drop to " + toAddress + " successful !!");
	    return(1);
	} else {
	    logger.info("Send " + amount + " drop to " + toAddress + " failed !!");
	    return(0);
	}
    }
    

    public TCli() {
	super();
    }    

    public long checkBalance(String password) {	
	long aBalance;
	aBalance = getBalanceCli(new String [] {password});	
        return aBalance;
    }

    public long sendCoin(String[] parameters) {	
	long status;
	status = sendCoinCli(parameters);
        return status;
    }

    
    
}
