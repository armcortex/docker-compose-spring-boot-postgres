package com.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.demo.model.Item;
import com.demo.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;

import java.util.Optional;

@RestController
@RequestMapping("/item")
public class ItemController {

    @Autowired
    private ItemService itemService;

    @Operation(summary="Add a new item", description="Creates a new item in the database")
    @ApiResponse(responseCode="200", description="Item created",
                    content={@Content(mediaType="application/json",
                    schema=@Schema(implementation=Item.class))})
    @PostMapping
    public Item addItem(@RequestBody Item item) {
        return itemService.saveItem(item);
    }

    @Operation(summary="Get an item by ID", description="Returns a single item")
    @ApiResponse(responseCode="200", description="Item found",
                    content={@Content(mediaType="application/json",
                    schema=@Schema(implementation=Item.class))})
    @ApiResponse(responseCode="404", description="Item not found")
    @GetMapping
    public Optional<Item> getItemById(@Parameter(description="ID of the item to be obtained", required=true)
                                      @RequestParam(name="id") long id) {
        return itemService.getItemById(id);
    }
}
