package org.tron.emb.apps;

import java.util.List;
import java.util.Arrays;
import java.util.concurrent.atomic.AtomicLong;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.util.UriComponentsBuilder;
import org.tron.emb.apps.model.TCliDS;
import org.tron.emb.apps.model.UserAccount;
import org.tron.emb.apps.model.sendCoin;
import org.tron.emb.apps.model.res;
import org.tron.emb.apps.model.BalData;

@RestController
public class CliRunController {

    @RequestMapping(value = "/sendcoin/", method = RequestMethod.POST)
    public ResponseEntity<res> sendCoin(@RequestBody sendCoin sendData, UriComponentsBuilder ucBuilder) {
        if ((sendData.getToaddress()=="") || (sendData.getPassword()=="") || (sendData.getAmount()=="")){
            //return new ResponseEntity(HttpStatus.NO_CONTENT);
	    return new ResponseEntity(HttpStatus.NOT_FOUND);

        }
	System.out.println("Toaddress : "+ sendData.getToaddress() + " Password : " + sendData.getPassword() +" Amount : " + sendData.getAmount()+"\n");
	TCli tcli = new TCli();
	String[] parameters = {sendData.getPassword(), sendData.getToaddress(), sendData.getAmount()};
    	Long status = tcli.sendCoin(parameters);

	if(status == 1){
	    res ResData = new res("OK");
	    return new ResponseEntity<res>(ResData, HttpStatus.OK);
	}
	else{
	    res ResData = new res("FAILED");
	    return new ResponseEntity<res>(ResData, HttpStatus.OK);
	}
	
        // HttpHeaders headers = new HttpHeaders();
        // headers.setLocation(ucBuilder.path("/api/test/{id}").buildAndExpand(124).toUri());
        // return new ResponseEntity<String>(headers, HttpStatus.CREATED);	
    }

    
    @RequestMapping(value = "/bal/", method = RequestMethod.POST)
    public ResponseEntity<BalData> getBalance(@RequestBody UserAccount AccData, UriComponentsBuilder ucBuilder) {
        if ((AccData.getAddress()=="") || (AccData.getPassword()=="")){
            //return new ResponseEntity(HttpStatus.NO_CONTENT);
	    return new ResponseEntity(HttpStatus.NOT_FOUND);

        }	
	System.out.println("Address : "+ AccData.getAddress() + " Password : " + AccData.getPassword() +"\n");

	TCli tcli = new TCli();
    	Long balance = tcli.checkBalance(AccData.getPassword());
	//System.out.println("Balance : "+ Long.toString(balance) + "\n");

	
    	BalData balData = new BalData(Long.toString(balance));
        return new ResponseEntity<BalData>(balData, HttpStatus.OK);
	
        // HttpHeaders headers = new HttpHeaders();
        // headers.setLocation(ucBuilder.path("/api/test/{id}").buildAndExpand(124).toUri());
        // return new ResponseEntity<String>(headers, HttpStatus.CREATED);	
    }

    
}


