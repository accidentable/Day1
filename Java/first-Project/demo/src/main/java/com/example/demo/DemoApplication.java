package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.example.demo.company.Company;


@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {

        SpringApplication.run(DemoApplication.class, args);

        Company company = new Company("Samsung", "Suwon");
        company.setFinancialStatement("200조", "50조");
        company.showRevenue();
    }

}
