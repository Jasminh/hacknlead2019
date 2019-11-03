package com.slavery.connect;

import java.net.UnknownHostException;
import java.util.ArrayList;
import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.ServerAddress;

import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;

import org.bson.Document;
import java.util.Arrays;
import com.mongodb.Block;

import com.mongodb.client.MongoCursor;
import static com.mongodb.client.model.Filters.*;
import com.mongodb.client.result.DeleteResult;
import static com.mongodb.client.model.Updates.*;
import com.mongodb.client.result.UpdateResult;
import java.util.ArrayList;
import java.util.List;


public class DBConnection {

public static void main(String[] args) throws UnknownHostException{
        
		/*
		 * // Create seed data
		 * 
		 * List<Document> seedData = new ArrayList<Document>();
		 * 
		 * seedData.add(new Document("decade", "1970s") .append("artist", "Debby Boone")
		 * .append("song", "You Light Up My Life") .append("weeksAtOne", 10) );
		 * 
		 * seedData.add(new Document("decade", "1980s") .append("artist",
		 * "Olivia Newton-John") .append("song", "Physical") .append("weeksAtOne", 10)
		 * );
		 * 
		 * seedData.add(new Document("decade", "1990s") .append("artist",
		 * "Mariah Carey") .append("song", "One Sweet Day") .append("weeksAtOne", 16) );
		 */

        // Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname
       
        MongoClientURI uri  = new MongoClientURI("mongodb://89.206.118.20:27017/db"); 
        MongoClient client = new MongoClient(uri);
        MongoDatabase db = client.getDatabase(uri.getDatabase());
        
        /*
         * First we'll add a few songs. Nothing is required to create the
         * songs collection; it is created automatically when we insert.
         */
        
       // MongoCollection<Document> songs = db.getCollection("songs");

        // Note that the insert method can take either an array or a document.
        
        //songs.insertMany(seedData);
       
      
        // Only close the connection when your app is terminating

        client.close();
    }
}
