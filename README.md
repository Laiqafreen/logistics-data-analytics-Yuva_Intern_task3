# Task 3 Summary Description:Advanced Data Analysis and Visualization in Logistics

Week 3 shifts the focus toward exploratory data analysis (EDA) and multi-variable statistical visualization to evaluate performance metrics across last-mile delivery operations. While previous phases established strategic KPIs and built automated data cleaning pipelines, this task leverages clean dispatch logs to uncover underlying operational trends, financial cost drivers, and transit bottlenecks that impact overall service level agreement (SLA) compliance.

The analytical framework executes through a structured 5-stage pipeline:

1. Data Ingestion: Loads clean dispatch records containing metrics such as route mileage, package volume, actual travel duration, fuel costs, labor expenses, and drop-off delay minutes.

2. Statistical Summary: Computes central tendencies and dispersion measures—including means, medians, standard deviations, and interquartile ranges—to establish reliable baseline performance indicators across all delivery routes.

3. Correlation Modeling: Generates a pairwise Pearson correlation matrix to evaluate interdependencies between features, pinpointing how route distance directly inflates fuel expenditure ($r \approx 0.91$) and how package payload sizes drive delivery delays.

4. Visual Analytics: Renders multi-variable charts using Python libraries (pandas, seaborn, matplotlib). This includes transit duration distribution histograms to identify route delays, distance-versus-fuel scatter plots to track cost scaling, and annotated heatmaps to visualize complex feature interactions.

5. Strategic Insights: Translates graphical outputs into actionable supply chain recommendations, such as implementing spatial route clustering to cap travel distances under 25 km and setting load limits per delivery van.The complete workflow is implemented via Python, providing visual charts and documentation to support data-driven decision-making in logistics management.

The complete workflow is implemented via Python, providing visual charts and documentation to support data-driven decision-making in logistics management.   
