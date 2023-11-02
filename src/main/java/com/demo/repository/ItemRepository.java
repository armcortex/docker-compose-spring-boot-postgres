package com.demo.repository;

import com.demo.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;
public interface ItemRepository extends JpaRepository<Item, Long> {
}