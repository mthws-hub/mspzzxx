package ec.espe.edu.contactsbook.model;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;
/**
 *
 * @author Mathews Pastor, The POOwer Rangers Of Programming
 */
public class MongoConection {
    private static final String CONNECTION_STRING = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/";
    private static final String DATABASE_NAME = "ContactBook";
    
    public static MongoDatabase getDatabase() {
        MongoClient client = MongoClients.create(CONNECTION_STRING);
        return client.getDatabase(DATABASE_NAME);
    }
}
