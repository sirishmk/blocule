package org.tron.emb.apps.model;

public class res {

    private String req;

    public res(){
	req = "";
    }
    
    public res(String req){
	this.req = req;
    }

    public String getReq(){
	return req;
    }
    
}
