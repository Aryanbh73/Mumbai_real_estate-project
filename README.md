# Mumbai Real Estate Analysis

## Project Background Overview

The Mumbai real estate market is one of the most dynamic and high-value property sectors in India. Prices vary significantly based on location, property type, amenities, and BHK configuration.
This project uses real estate listing data for Mumbai to perform exploratory data analysis (EDA), visualization, and dashboard creation in Power BI and Python.

The analysis aims to:

Background & Overview
The Mumbai real estate market is one of the most dynamic and high-value property sectors in India. Prices vary significantly based on location, property type, amenities, and BHK configuration.
This project uses real estate listing data for Mumbai to perform exploratory data analysis (EDA), visualization, and dashboard creation in Power BI and Python.

The analysis aims to:

- Understand pricing patterns across locations and property types

- Identify premium locations and market segments

- Evaluate the impact of amenities and property size on price

- Provide data-driven recommendations for buyers, sellers, and investors

##Data Structure Overview

The dataset contains 6,347 property listings with the key columns:

&nbsp;&nbsp;&nbsp;<img width="273" height="247" alt="data over1" src="https://github.com/user-attachments/assets/fb84d088-060a-42f4-b3b0-94a214b71521" />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img width="273" height="249" alt="data over2" src="https://github.com/user-attachments/assets/37f38741-0a4d-4eb3-b45d-05849053c083" />

&nbsp;&nbsp;&nbsp;<img width="305" height="249" alt="data over3" src="https://github.com/user-attachments/assets/c572d788-73f5-450b-ac31-1f77e6a1cee2" />

## Executive Summary

### Price and Amenities:

The price and amenities analysis demonstrates that properties with premium facilities command significantly higher valuations. Listings with amenities such as gymnasiums, swimming pools, and dedicated car parking consistently exceed the citywide average price per sq. ft. of ₹13,555, often reaching ₹18,000–₹20,000 per sq. ft. Properties offering four or more key amenities tend to fall into the high-price segment, with average total prices above ₹2 crore. Interestingly, some emerging suburbs like Mira Road West and Kalyan West combine extensive amenities with competitive per sq. ft. prices around ₹9,000–₹11,000, making them attractive to budget-conscious buyers. In contrast, luxury zones like Malabar Hill and Bandra West maintain per sq. ft. rates above ₹40,000, where amenities act as a baseline expectation rather than a differentiator.

<img width="875" height="450" alt="Price and Amenities Insights" src="https://github.com/user-attachments/assets/749e44ea-6f6d-4296-b4fb-1729992a81e3" />

- Average Citywide Price per Sq. Ft.: ₹13,555

- Premium Amenity Impact: 4+ amenities → ₹18,000–₹20,000 per sq. ft.

- Average Price for 4+ Amenity Properties: ₹2 crore+

- Value Locations: Mira Road West & Kalyan West (~₹9,000–₹11,000 per sq. ft.)

- Luxury Clusters: Malabar Hill & Bandra West (>₹40,000 per sq. ft.)

- Top Amenities Driving Price Premiums: Gymnasium, Swimming Pool, Car Parking

- High-value amenities (gym, pool, car parking, gardens) correlate with higher property prices.

- Properties with more amenities are typically found in higher price categories.

- Suburban locations with strong amenity offerings provide better price-to-value ratios.

- In luxury market segments, amenities are expected but location remains the key price driver.

- Amenities improve market appeal and act as price enhancers in competitive locations.

### Property Type & Market Segmentation:

The macro-level analysis of the Mumbai real estate market reveals a highly segmented property landscape with clear pricing tiers. Out of 6,347 listings, the average property price is ₹1.51 crore, with prices ranging from ₹20 lakh to ₹4.2 crore, and an average price per sq. ft. of ₹13,555. A majority of listings fall into medium (₹80 lakh – ₹1.5 crore) and high-price (₹1.5 crore – ₹2.5 crore) categories, with 46% classified as high-price properties. 2BHK units make up 41% of the market, followed by 3BHK at 32%, while 4BHK+ units represent only 8% but command up to 3× the price per sq. ft. Apartments dominate the market with over 85% share, while villas and independent houses together account for less than 5%. Geographically, Khargar (9%), Thane West (7%), and Mira Road West (6%) lead in listing volumes, while prime areas like Malabar Hill and Worli hold per sq. ft. valuations exceeding ₹40,000.

<img width="889" height="499" alt="Property Type   Market Segmentation" src="https://github.com/user-attachments/assets/8ce5b798-046a-46ac-ab7e-6dab26b1d33e" />

- Average Price: ₹1.51 crore (Range: ₹20 lakh – ₹4.2 crore)

- Price Category Split: 46% high-price, 38% medium-price, 16% low-price

- BHK Split: 2BHK (41%), 3BHK (32%), 4BHK+ (8%)

- Property Type Split: Apartments (85%), Villas + Independent Houses (<5%)

- Top Locations by Listing Volume: Khargar (9%), Thane West (7%), Mira Road West (6%)

- Highest Per Sq. Ft. Pricing: Malabar Hill, Worli (>₹40,000 per sq. ft.)

- Most properties fall into medium to high-price categories, aligning with Mumbai’s overall premium market.

- 2BHK and 3BHK units dominate supply, catering to middle-income and upper-middle-income demand.

- Larger configurations (4BHK and above) are scarce but priced significantly higher.

- Apartments are the dominant property type, with minimal presence of villas or independent houses.

- Suburban hubs (Khargar, Thane West, Mira Road West) lead in listing volumes.

- Prime south and central Mumbai areas hold the highest per sq. ft. valuations.

## Insights Deep Dive
  
Macro View — Citywide Trends
- Khargar, Thane West, Mira Road West emerge as top listing hubs with varied price segments.

- Price per sq. ft. varies widely between low-budget and premium locations.

- Majority of listings fall in Medium to High price categories.

Location-Wise Price Patterns
- South and central Mumbai pockets show very high per sq. ft. prices.

- Some suburban locations with high amenities still have competitive pricing.

BHK-Based Observations
- 2BHK and 3BHK properties dominate listings.

- Larger BHKs (5BHK, 6BHK, 7BHK) show sharp price jumps but limited availability.

Amenities Impact
- Locations with Gymnasium, Swimming Pool, Car Parking, and Parks command higher average prices.

- Amenities contribute to price premiums but also correlate with property size.

Price vs Area Relationship
- Properties under ~2,000 sq. ft. show wide price dispersion, indicating location/amenity influence over pure size metrics.

## Recommendations

For Buyers:

- Explore suburban regions like Mira Road West or Kalyan West for better price-to-amenity ratios.

- Consider resale properties for better negotiation margins in premium areas.

For Sellers:

- Highlight amenities and unique features in listings — they have proven price uplift potential.

- Price competitively in saturated mid-tier locations to improve sale velocity.

For Investors:

- Focus on emerging hubs with infrastructure projects — these have the potential for strong appreciation.

- Monitor high-price clusters for potential luxury market investment.

### Tech Stack & Tools
  
- Python (Pandas, Matplotlib, Seaborn) — Data cleaning, EDA, and visualization

- Power BI — Interactive dashboards for macro & micro analysis

- Excel — Raw Mumbai property listings data and add ons
