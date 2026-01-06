package ec.edu.espe.repasoprueba.utils;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;    
/**
 *
 * @author Mathews Pastor, The POOwer Rangers Of Programming
 */
public class MongoConnection {

    private static MongoConnection instance;
    private MongoClient mongoClient;
    private MongoDatabase database;

    private static final String CONNECTION_STRING = "mongodb+srv://Mathews:Mathews2007@cluster0.6l9ibfh.mongodb.net/?appName=Cluster0";
    private static final String DATABASE_NAME = "ArtGalleryDB";

    private MongoConnection() {
        try {
            // Crea la conexión al cliente de MongoDB
            mongoClient = MongoClients.create(CONNECTION_STRING);
            database = mongoClient.getDatabase(DATABASE_NAME);
            System.out.println("Conexión a MongoDB exitosa.");
        } catch (Exception e) {
            System.err.println("Error conectando a MongoDB: " + e.getMessage());
        }
    }

    // Método estático para obtener la única instancia
    public static MongoConnection getInstance() {
        if (instance == null) {
            instance = new MongoConnection();
        }
        return instance;
    }

    // Retorna la base de datos para realizar operaciones
    public MongoDatabase getDatabase() {
        return database;
    }

    // Cierra la conexión al finalizar la aplicación
    public void close() {
        if (mongoClient != null) {
            mongoClient.close();
            System.out.println("Conexión a MongoDB cerrada.");
        }
    }
}
