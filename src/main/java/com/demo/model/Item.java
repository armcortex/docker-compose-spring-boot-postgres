package com.demo.model;
import jakarta.persistence.*;

@Entity
@Table(name="items")
public class Item {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name="first_name")
    private String fname;

    @Column(name="last_name")
    private String lname;

    @Column(name="country")
    private String country;

    public Item() {

    }
    public Item(String fname, String lname, String country) {
        this.fname = fname;
        this.lname = lname;
        this.country = country;
    }

    public long getId() {
        return id;
    }

    public String getLname() {
        return lname;
    }

    public  String getFname() {
        return fname;
    }

    public  String getCountry() {
        return country;
    }
}
