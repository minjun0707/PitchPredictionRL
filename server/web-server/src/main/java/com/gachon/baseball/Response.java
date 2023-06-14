package com.gachon.baseball;

import lombok.Data;

@Data
public class Response {
    public String response;

    public Response(String response) {
        this.response = response;
    }
}
