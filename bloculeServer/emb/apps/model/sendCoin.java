package org.tron.emb.apps.model;

public class sendCoin {

    private String toaddress;
    private String password;
    private String amount;

    public sendCoin(){
	toaddress = "";
	password = "";
	amount = "";
    }
    
    public sendCoin(String toaddress, String password){
	this.toaddress = toaddress;
	this.password = password;
	this.amount = amount;	
	
    }

    public String getToaddress(){
	return toaddress;
    }
    
    public String getPassword(){
	return password;
    }

    public String getAmount(){
	return amount;
    }
    
    
}
