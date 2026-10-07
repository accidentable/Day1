package com.example.demo.company;

public class Company {
    String name; // 회사 이름
    String location; // 회사 위치
    int age; // 회사 나이
    String revenue; // 현재 매출
    String netIncome; // 영업 이익

    public Company(String name, String location){ // 매개변수를 가진 생성자
        this.name = name;
        this.location = location;
    }

    public void setFinancialStatement(String revenue, String netIncome){ //재무제표 설정
        this.revenue = revenue;
        this.netIncome = netIncome;
    }
    public void showRevenue() {
        System.out.println(name + "의 매출은" + revenue + "입니다.");
    }
}
