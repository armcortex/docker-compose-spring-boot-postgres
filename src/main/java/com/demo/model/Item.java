package com.demo.model;
import jakarta.persistence.*;

@Entity
@Table(name="items")
public class Item {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private long id;

    @Column(name="First Name")
    private String fname;

    @Column(name="Last Name")
    private String lname;

    @Column(name="Country")
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
