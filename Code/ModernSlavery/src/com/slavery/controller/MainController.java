package com.slavery.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import com.mongodb.client.model.Filters;
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
	

	@RequestMapping(value = "/GetCountry", method = RequestMethod.POST)
	@ResponseBody
    public String GetCountry(@RequestParam("product") String product,ModelMap model) {
		System.out.print("Entered:: "+product);
		List<String> countryListForProduct = new ArrayList<String>();
		DBCollection coll = MongoFactory.getCollection("goodexplorers", "products");
		
		BasicDBObject whereQuery = new BasicDBObject();
		whereQuery.put("product", product);
		DBCursor cursor = coll.find(whereQuery);
		while(cursor.hasNext()) {
			DBObject dbObject = cursor.next();
			countryListForProduct = (List<String>) dbObject.get("countries");
		}
		
		model.addAttribute("countryList", countryListForProduct);
        return "from java";
	}
	
	@RequestMapping(value = "/getChartDetails", method = RequestMethod.POST)
	@ResponseBody
    public String getChartDetails(@RequestParam("country") String country,ModelMap model) {
		
		DBCollection coll = MongoFactory.getCollection("goodexplorers", "countries");
		List chartDataList = new ArrayList();
		String data="";
		 
		BasicDBObject whereQuery = new BasicDBObject();
		whereQuery.put("country", "Afghanistan");
		DBCursor cursor = coll.find(whereQuery);
		
        while(cursor.hasNext()) {           
            DBObject dbObject = cursor.next();
            

    		SlaveryObj slaveryObj = new SlaveryObj();
			slaveryObj.setCountry(dbObject.get("country").toString());
			slaveryObj.setFactors(dbObject.get("factors").toString());
			 
			data = dbObject.get("factors").toString();
			
			chartDataList.add(slaveryObj);
        }
        
       return data;
	}
	
}
