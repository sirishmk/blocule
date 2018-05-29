package org.tron.emb.apps.model;

public class UserAccount {

    private String address;
    private String password;

    public UserAccount(){
	address = "";
	password = "";
    }
    
    public UserAccount(String address, String password){
	this.address = address;
	this.password = password;	
    }

    public String getAddress(){
	return address;
    }
    
    public String getPassword(){
	return password;
    }

    
}
