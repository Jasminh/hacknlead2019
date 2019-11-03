package com.slavery.pojo;

import java.io.Serializable;
import java.util.List;

public class SlaveryObj implements Serializable {
 
    private static final long serialVersionUID = 1L;
 
    private String productName;
    private String country;
    private List<String> countryList;
    private String factors;
    
	public String getFactors() {
		return factors;
	}
	public void setFactors(String factors) {
		this.factors = factors;
	}
	public String getProductName() {
		return productName;
	}
	public void setProductName(String productName) {
		this.productName = productName;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	public List<String> getCountryList() {
		return countryList;
	}
	public void setCountryList(List<String> countryList) {
		this.countryList = countryList;
	}
    
    
	
	

}
