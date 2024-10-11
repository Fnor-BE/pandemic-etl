DROP TABLE Dim.Country

CREATE TABLE Dim.Country(
	CountryID INT PRIMARY KEY IDENTITY,
	Country NVARCHAR(50),
	ProvinceState NVARCHAR(50),
	WHORegion NVARCHAR(50),
	Latitude DECIMAL(10, 6),
	Longitude DECIMAL(10, 6),
)
