package ec.edu.espe.repasoprueba.model;

import java.util.List;
import org.bson.Document;

/**
 *
 * @author Mathews Pastor, The POOwer Rangers Of Programming
 */
public class Painting {

    private String id;
    private String name;
    private double price;
    private List<String> colors;
    private double priceWithIva;

    public Painting(String id, String name, double price, List<String> colors, double priceWithIva) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.colors = colors;
        this.priceWithIva = priceWithIva;
    }
    
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public List<String> getColors() {
        return colors;
    }

    public void setColors(List<String> colors) {
        this.colors = colors;
    }

    public double getPriceWithIva() {
        return priceWithIva;
    }

    public void setPriceWithIva(double priceWithIva) {
        this.priceWithIva = priceWithIva;
    }

    @Override
    public String toString() {
        return name + " ($" + priceWithIva + ")";
    }
}
