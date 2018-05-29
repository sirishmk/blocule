package org.tron.emb.apps.model;

public class TCliDS {
 
    private long id;     

    private String name;
    
    private long balance;
    
    private double rID;
 
    public TCliDS(){
        id=0;
    }
     
    public TCliDS(long id, String name, long balance,  double rID){
        this.id = id;
	this.name = name;
        this.balance = balance;
	this.rID = rID;

    }
     
    public long getId() {
        return id;
    }

    public double getrID() {
        return rID;
    }
    
    public String getName() {
        return name;
    }
 
    public void setName(String name) {
        this.name = name;
    }
 
 
    public double getBalance() {
        return balance;
    }

    @Override
    public String toString() {
        return "TCliDS [id=" + id + ", name=" + name + ", balance=" + balance
                + ", rID=" + rID + "]";
    }
 
}
