package com.gachon.baseball;

import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RestController
@Slf4j
public class BaseBallApi {


    @CrossOrigin("*")
    @PostMapping("/api/pitch-detection")
    public String api(@RequestBody DetectionRequest detectionRequest) throws JsonProcessingException {

        detectionRequest.changeForJson();
        log.info(detectionRequest.toString());
        RestTemplate restTemplate = new RestTemplate();

        //플라스크 api 서버 url
        String url = "http://localhost:5000/api/flask/pitch-detection";

        //header 설정
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.setContentType(MediaType.APPLICATION_JSON);

        //요청 객체
        HttpEntity<?> requestMessage = new HttpEntity<>(detectionRequest, httpHeaders);

        //플라스크 api 서버에 요청
        HttpEntity<String> response = restTemplate.postForEntity(url, requestMessage, String.class);
        log.info(response.getBody());
        log.info("플라스크 result 로그받음 : " +response.getBody());

        return response.getBody();

    }



//    @CrossOrigin("*")
//    @PostMapping("/api/reinforcement")
//    public String reinfrocementApi() throws JsonProcessingException {
//
//        //formResponse.changeForJson();
//        //log.info(formResponse.toString());
//        RestTemplate restTemplate = new RestTemplate();
//
//        //플라스크 api 서버 url
//        String url = "http://localhost:5000/api/flask/reinforcement";
//
//        //header 설정
//        HttpHeaders httpHeaders = new HttpHeaders();
//        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//
//        //요청 객체
//        HttpEntity<?> requestMessage = new HttpEntity<>(formResponse, httpHeaders);
//
//        //플라스크 api 서버에 요청
//        HttpEntity<String> response = restTemplate.postForEntity(url, requestMessage, String.class);
//        log.info(response.getBody());
//        log.info("플라스크 result 로그받음 : " +response.getBody());
//
//        return response.getBody();
//
//    }













//    @CrossOrigin("*")
//    @GetMapping("/api/test")
//    public String test(){
//        log.info("요청왔음");
//        return "test Success";
//    }
//
//
//    @CrossOrigin("*")
//    @GetMapping("/api/test2")
//    public String test2(){
//        log.info("파이썬 request 테스트");
//        RestTemplate restTemplate = new RestTemplate();
//        String url = "http://localhost:5000";
//
//        //header 설정
//        HttpHeaders httpHeaders = new HttpHeaders();
//        httpHeaders.setContentType(MediaType.APPLICATION_JSON);
//
//        //요청 객체
//        HttpEntity<?> requestMessage = new HttpEntity<>(httpHeaders);
//
//        //플라스크 api 서버에 요청
//        HttpEntity<String> response = restTemplate.getForEntity(url, String.class);
//        return "python test success";
//    }



}
