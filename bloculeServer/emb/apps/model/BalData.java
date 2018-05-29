package org.tron.emb.apps.model;

public class BalData {

    private String balance;

    public BalData(){
	balance = "";
    }
    
    public BalData(String balance){
	this.balance = balance;
    }

    public String getBalance(){
	return balance;
    }
    
}
