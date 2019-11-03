package com.slavery.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.slavery.pojo.SlaveryObj;

@Controller
@RequestMapping("/hello")
public class MainController {
	
	
	@RequestMapping(method = RequestMethod.GET)
	public List getProductName(ModelMap model) {
		List dataList = new ArrayList();
		 
		/*
		 * model.addAttribute("message", "Hello Spring MVC Framework!"); return "hello";
		 */
		//DBCollection coll = MongoFactory.getCollection("myDB", "myCollection");
		DBCollection coll = MongoFactory.getCollection("goodexplorers", "products");
		
		 
        // Fetching cursor object for iterating on the database records.
        DBCursor cursor = coll.find();  
        while(cursor.hasNext()) {           
            DBObject dbObject = cursor.next();
            

    		SlaveryObj slaveryObj = new SlaveryObj();
			slaveryObj.setProductName(dbObject.get("product").toString());
			slaveryObj.setCountryList((List<String>) dbObject.get("countries"));
			 
			dataList.add(slaveryObj);
        }
       model.addAttribute("dataList", dataList);
       return dataList;  
	   }
	

	@RequestMapping(value = "/abc", method = RequestMethod.GET)
    public String addStudent() {
		System.out.print("Entered");
		List user_list = new ArrayList();
        DBCollection coll = MongoFactory.getCollection("myDB", "myCollection");
 
        // Fetching cursor object for iterating on the database records.
        DBCursor cursor = coll.find();  
        while(cursor.hasNext()) {           
            DBObject dbObject = cursor.next();
            
            SlaveryObj user = new SlaveryObj();
            user.setProductName(dbObject.get("product_name").toString());
            user.setCountry(dbObject.get("country").toString());
 
            // Adding the user details to the list.
            user_list.add(user);
           
        }
        
        return null;
	}
	
}
