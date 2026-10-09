/*
    Day05
    기업(Company) 테이블과 산업(industry) 테이블을 어떻게 구성할 수 있을까?

    이름은 업무 데이터이기 때문에 변할 수 있는 여지가 많다.
    하지만 ID(숫자)를 인조키(혹은 자연키-종목코드 등)으로 두면 안정적으로 오래 유지 될 수 있고
    PK-FK는 안정적으로 오래 유지되어 수정할 일이 적은 컬럼을 선택해야 한다.
    -- day06 수정 industry 가 company보다 먼저 생성되어야 함
    그렇지 않을 경우, company의 FOREIGN key가 참조할 대상이 없어서 에러.
*/

CREATE TABLE industry(
    industryName VARCHAR(255) not NULL,
    industryID INT not NULL,
    --numberOfCompanies INT not NULL, : derived value(계산 가능한 값)
    PRIMARY KEY (industryID)
);

CREATE TABLE company(
    companyName VARCHAR(255) not NULL,
    companyID INT not NULL,
    industryID INT not NULL,
    revenue INT not NULL,
    netIncome INT not NULL,

    PRIMARY KEY (companyID),
    FOREIGN KEY (industryID)
    REFERENCES industry(industryID)
);

