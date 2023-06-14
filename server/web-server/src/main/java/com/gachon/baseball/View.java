package com.gachon.baseball;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@Slf4j
public class View {

    @CrossOrigin("*")
    @GetMapping("/reinforcement")
    public String basicPage() {
        return "reinforcement";
    }

    @CrossOrigin("*")
    @GetMapping("/pitch-tipping")
    public String viewPitchTipping() {
        return "pitch-tipping";
    }
}
