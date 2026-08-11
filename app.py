import streamlit as st
import pandas as pd
import joblib
import textwrap


# =========================================================
# LOAD MODEL AND DATA
# =========================================================

model = joblib.load("Best_House_Price_Model.pkl")
model_columns = joblib.load("model_columns.pkl")

df = pd.read_csv("House_Prediction_Cleaned.csv")


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Property Valuation",
    page_icon="🏠",
    layout="wide",
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
   COLORFUL THEME
   ========================================================= */

@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(120deg, #fdf2ff 0%, #f0f7ff 25%, #fff8ec 50%, #f0fff7 75%, #fdf2ff 100%);
    background-size: 300% 300%;
    animation: gradientShift 22s ease infinite;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #f3e8ff 0%, #fde2ec 100%);
    border-right: 1px solid #eadcfb;
}

[data-testid="stSidebar"] * {
    color: #6d28d9 !important;
}

.block-container {
    padding-top: 1rem;
}

[data-testid="stHeader"] {
    background: transparent;
}

/* Tabs — soft pastel palette, no box outline, color only */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: transparent;
    border-radius: 14px;
    padding: 10px 20px;
    font-weight: 700;
    border: none;
    box-shadow: none;
}

.stTabs [aria-selected="true"] {
    background: transparent !important;
    color: #6d28d9 !important;
    border: none !important;
    box-shadow: none !important;
}

.stTabs [aria-selected="true"] p {
    color: #6d28d9 !important;
    font-weight: 800 !important;
}

[data-baseweb="tab-highlight"] {
    background-color: #d8b4fe !important;
}

[data-baseweb="tab-border"] {
    background-color: #eee3fb !important;
}

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 900;
    margin-bottom: 5px;
    background: linear-gradient(90deg, #7c3aed, #db2777, #f59e0b, #10b981);
    background-size: 300% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: gradientShift 8s linear infinite;
}

.subtitle {
    text-align: center;
    color: #7c3aed;
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 15px;
    color: #6d28d9;
    border-left: 6px solid #f472b6;
    padding-left: 12px;
}

.price-box {
    padding: 35px;
    border-radius: 24px;
    text-align: center;
    background: linear-gradient(135deg, #f3e8ff 0%, #fde2ec 50%, #fff3d6 100%);
    border: 2px solid #eadcfb;
    box-shadow: 0 10px 26px rgba(124, 58, 237, 0.14);
}

.price {
    font-size: 46px;
    font-weight: 900;
    color: #6d28d9;
}

.price-sub {
    color: #9d5fc2;
    font-size: 15px;
    font-weight: 600;
}

.value-card {
    background: linear-gradient(160deg, #ffffff, #fdf2ff);
    border-radius: 18px;
    padding: 25px 15px;
    text-align: center;
    box-shadow: 0 8px 22px rgba(124, 58, 237, 0.15);
    min-height: 170px;
    border: 2px solid #f3e8ff;
    transition: transform 0.15s ease;
}

.value-medal {
    font-size: 35px;
    margin-bottom: 8px;
}

.value-city {
    font-size: 21px;
    font-weight: 800;
    color: #6d28d9;
    margin-bottom: 8px;
}

.value-price {
    font-size: 16px;
    color: #db2777;
    font-weight: 700;
}

.budget-card {
    background: linear-gradient(160deg, #ffffff, #fff7ed);
    padding: 25px;
    border-radius: 18px;
    border: 2px solid #fde68a;
    box-shadow: 0 6px 18px rgba(245, 158, 11, 0.18);
    min-height: 145px;
}

.budget-card-title {
    color: #b45309;
    font-size: 14px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.budget-card-value {
    color: #7c3aed;
    font-size: 30px;
    font-weight: 900;
    margin-top: 12px;
}

.budget-card-subtitle {
    color: #a16207;
    font-size: 13px;
    margin-top: 5px;
}

.howto-card {
    background: linear-gradient(135deg, #ffffff, #ecfeff);
    border-radius: 18px;
    padding: 22px 26px;
    border: 2px solid #a5f3fc;
    box-shadow: 0 6px 18px rgba(6, 182, 212, 0.15);
    margin-bottom: 25px;
}

.howto-title {
    font-size: 18px;
    font-weight: 800;
    color: #0e7490;
    margin-bottom: 12px;
}

.howto-step {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 10px;
}

.howto-num {
    background: linear-gradient(135deg, #7c3aed, #db2777);
    color: white;
    font-weight: 800;
    font-size: 13px;
    min-width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(219, 39, 119, 0.4);
}

.howto-text {
    color: #374151;
    font-size: 14.5px;
    padding-top: 2px;
}

/* Button — matches the pastel palette */
.stButton > button {
    background: linear-gradient(90deg, #a78bfa, #f472b6, #fbbf24);
    background-size: 200% auto;
    color: white;
    font-weight: 800;
    border: none;
    border-radius: 14px;
    padding: 12px 0;
    box-shadow: 0 6px 16px rgba(167, 139, 250, 0.30);
    transition: background-position 0.4s ease, transform 0.15s ease;
}

.stButton > button:hover {
    background-position: right center;
    transform: translateY(-2px);
    color: white;
}

/* Metrics */
[data-testid="stMetric"] {
    background: linear-gradient(160deg, #ffffff, #f3e8ff);
    border-radius: 14px;
    padding: 12px 10px;
    border: 2px solid #e9d5ff;
    box-shadow: 0 4px 12px rgba(124, 58, 237, 0.12);
}

[data-testid="stMetricValue"] {
    color: #7c3aed;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# TABS (replaces sidebar navigation)
# =========================================================

tab1, tab2, tab3 = st.tabs(
    ["🏠 Price Prediction", "📊 Dashboard", "🤖 Model Performance"]
)


# =========================================================
# TAB 1: PRICE PREDICTION
# =========================================================

with tab1:

    st.markdown(
        '<div class="main-title">'
        '🏠House Price Prediction'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        ' powered by Machine Learning'
        '</div>',
        unsafe_allow_html=True
    )

    # =====================================================
    # HOW TO USE THIS CARD
    # =====================================================

    howto_html = (
        '<div class="howto-card">'
        '<div class="howto-title">📋 How to use this tool</div>'

        '<div class="howto-step">'
        '<div class="howto-num">1</div>'
        '<div class="howto-text">Fill in the property details below '
        '&mdash; city, locality, size, building details, features, '
        'accessibility, and amenities.</div>'
        '</div>'

        '<div class="howto-step">'
        '<div class="howto-num">2</div>'
        '<div class="howto-text">Click <b>ESTIMATE PROPERTY VALUE</b> '
        'once every section looks right.</div>'
        '</div>'

        '<div class="howto-step">'
        '<div class="howto-num">3</div>'
        '<div class="howto-text">Review your estimated price below the '
        'button, along with a quick profile summary of the property.</div>'
        '</div>'

        '<div class="howto-step">'
        '<div class="howto-num">4</div>'
        '<div class="howto-text">Not sure how the estimate compares? '
        'Check the <b>Dashboard</b> tab for city-wise pricing, or the '
        '<b>Model Performance</b> tab to see how accurate this model is.</div>'
        '</div>'

        '</div>'
    )

    st.markdown(howto_html, unsafe_allow_html=True)

    # =====================================================
    # PROPERTY INFORMATION
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '🏡 Property Information'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        city = st.selectbox(
            "🏙️ City",
            sorted(df["City"].dropna().unique())
        )

    with col2:

        locality_options = sorted(
            df[df["City"] == city]["Locality"]
            .dropna()
            .unique()
        )

        locality = st.selectbox(
            "📍 Locality",
            locality_options
        )

    with col3:

        bhk = st.number_input(
            "🛏️ BHK",
            min_value=1,
            max_value=10,
            value=3
        )

    with col4:

        area_sqft = st.number_input(
            "📐 Area (sqft)",
            min_value=300,
            max_value=10000,
            value=1700,
            step=50
        )

    # =====================================================
    # BUILDING DETAILS
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '🏢 Building Details'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        bathrooms = st.number_input(
            "🛁 Bathrooms",
            min_value=1.0,
            max_value=10.0,
            value=2.0,
            step=0.5
        )

    with col2:

        total_floors = st.number_input(
            "🏢 Total Floors",
            min_value=1,
            max_value=30,
            value=5
        )

    with col3:

        floor_number = st.number_input(
            "🔢 Floor Number",
            min_value=1,
            max_value=30,
            value=3
        )

    with col4:

        property_age = st.number_input(
            "📅 Property Age",
            min_value=0,
            max_value=100,
            value=10
        )

    # =====================================================
    # PROPERTY FEATURES
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '✨ Property Features'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        parking_spaces = st.number_input(
            "🚗 Parking Spaces",
            min_value=0.0,
            max_value=10.0,
            value=1.0
        )

    with col2:

        balcony = st.number_input(
            "🌇 Balconies",
            min_value=0.0,
            max_value=10.0,
            value=1.0
        )

    with col3:

        furnishing = st.selectbox(
            "🛋️ Furnishing",
            sorted(df["Furnishing"].dropna().unique())
        )

    with col4:

        property_type = st.selectbox(
            "🏠 Property Type",
            sorted(df["Property_Type"].dropna().unique())
        )

    # =====================================================
    # ACCESSIBILITY
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '📍 Accessibility'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        distance_city = st.number_input(
            "🏙️ City Center (km)",
            min_value=0.0,
            max_value=50.0,
            value=7.0,
            step=0.1
        )

    with col2:

        metro_distance = st.number_input(
            "🚇 Metro Distance (km)",
            min_value=0.0,
            max_value=30.0,
            value=3.0,
            step=0.1
        )

    with col3:

        nearby_schools = st.number_input(
            "🏫 Nearby Schools",
            min_value=0.0,
            max_value=20.0,
            value=5.0
        )

    with col4:

        nearby_hospitals = st.number_input(
            "🏥 Nearby Hospitals",
            min_value=0,
            max_value=20,
            value=3
        )

    # =====================================================
    # AMENITIES
    # =====================================================

    st.markdown(
        '<div class="section-title">'
        '🛡️ Amenities & Safety'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        amenities_score = st.slider(
            "⭐ Amenities Score",
            1.0,
            10.0,
            5.0,
            0.5
        )

    with col2:

        security_score = st.slider(
            "🔐 Security Score",
            1,
            10,
            5
        )

    with col3:

        maintenance_cost = st.number_input(
            "🔧 Maintenance Cost",
            min_value=500,
            max_value=30000,
            value=6500,
            step=100
        )

    st.markdown("")

    # =====================================================
    # PREDICT BUTTON
    # =====================================================

    predict_button = st.button(
        "🔮 ESTIMATE PROPERTY VALUE",
        use_container_width=True
    )

    # =====================================================
    # PREDICTION
    # =====================================================

    if predict_button:

        user_data = pd.DataFrame({

            "City": [city],
            "Locality": [locality],
            "BHK": [bhk],
            "Area_sqft": [area_sqft],
            "Bathrooms": [bathrooms],
            "Total_Floors": [total_floors],
            "Floor_Number": [floor_number],
            "Parking_Spaces": [parking_spaces],
            "Balcony": [balcony],
            "Property_Age": [property_age],
            "Furnishing": [furnishing],
            "Property_Type": [property_type],
            "Distance_to_City_Center_km": [distance_city],
            "Metro_Distance_km": [metro_distance],
            "Nearby_Schools": [nearby_schools],
            "Nearby_Hospitals": [nearby_hospitals],
            "Amenities_Score": [amenities_score],
            "Security_Score": [security_score],
            "Maintenance_Cost": [maintenance_cost]
        })

        # =================================================
        # FEATURE ENGINEERING
        # SAME AS NOTEBOOK
        # =================================================

        user_data["Bath_BHK_Ratio"] = (
            user_data["Bathrooms"] /
            user_data["BHK"]
        )

        user_data["Total_Facilities"] = (
            user_data["Parking_Spaces"]
            + user_data["Balcony"]
            + user_data["Nearby_Schools"]
            + user_data["Nearby_Hospitals"]
        )

        user_data["Location_Score"] = (
            user_data["Nearby_Schools"]
            + user_data["Nearby_Hospitals"]
            - user_data["Distance_to_City_Center_km"]
            - user_data["Metro_Distance_km"]
        )

        # =================================================
        # CATEGORICAL ENCODING
        # =================================================
        # NOTE: We do NOT use pd.get_dummies() here.
        #
        # pd.get_dummies() on a single-row DataFrame is broken for
        # inference: with drop_first=True, a column that has only
        # ONE unique value (always true for 1 row) gets its dummy
        # dropped no matter what that value actually is. That means
        # every City/Locality/Furnishing/Property_Type selection was
        # silently being encoded as all-zeros (the reference/baseline
        # category used in training) -- so changing the dropdowns had
        # almost no effect on the predicted price.
        #
        # Instead, we build the one-hot columns manually against the
        # exact column names the model was trained on (model_columns),
        # which were produced in the notebook by:
        #   pd.get_dummies(X, drop_first=True, dtype=int)
        # =================================================

        categorical_inputs = {
            "City": city,
            "Locality": locality,
            "Furnishing": furnishing,
            "Property_Type": property_type
        }

        # Start from the numeric/engineered columns only
        categorical_cols = list(categorical_inputs.keys())
        encoded_data = user_data.drop(columns=categorical_cols)

        # Add every one-hot column the model expects, defaulting to 0
        for col in model_columns:
            if col not in encoded_data.columns:
                encoded_data[col] = 0

        # Set the correct dummy column to 1 for each selected category.
        # If "{col}_{value}" isn't in model_columns, it means that value
        # was the dropped baseline/reference category during training,
        # so leaving everything at 0 is the CORRECT encoding for it.
        for col_name, value in categorical_inputs.items():
            dummy_col = f"{col_name}_{value}"
            if dummy_col in encoded_data.columns:
                encoded_data[dummy_col] = 1

        # =================================================
        # MATCH TRAINING COLUMNS (order matters for the model)
        # =================================================

        user_data = encoded_data[model_columns]

        # =================================================
        # PREDICT PRICE
        # =================================================

        prediction = model.predict(user_data)[0]

        # =================================================
        # DISPLAY PRICE
        # =================================================

        st.markdown("---")

        st.markdown(
            '<div class="section-title">'
            '🎯 Estimated Property Value'
            '</div>',
            unsafe_allow_html=True
        )

        price_box_html = (
            '<div class="price-box">'
            f'<div class="price">₹ {prediction:,.0f}</div>'
            '<div class="price-sub">Estimated market value</div>'
            '</div>'
        )

        st.markdown(price_box_html, unsafe_allow_html=True)

        st.markdown("")

        st.metric(
            "🇮🇳 Estimated Property Price",
            f"₹ {prediction:,.0f}"
        )

        # =================================================
        # PROPERTY PROFILE
        # =================================================

        st.markdown("---")

        st.subheader("🏠 Property Profile")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.metric("City", city)

        with col2:
            st.metric("BHK", bhk)

        with col3:
            st.metric("Area", f"{area_sqft:,} sqft")

        with col4:
            st.metric("Bathrooms", bathrooms)

        with col5:
            st.metric("Property Type", property_type)

        st.success(
            "✅ Prediction generated successfully using "
            "the Random Forest model."
        )

        st.caption(
            "Note: The predicted value is an ML-based estimate "
            "and may differ from the actual market price."
        )


# =========================================================
# TAB 2: DASHBOARD
# =========================================================

with tab2:

    st.title("📊 Property Intelligence Dashboard")

    st.write(
        "Explore property prices, value-for-money cities, "
        "and properties available within your budget."
    )

    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    st.subheader("📌 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏠 Properties",
            f"{len(df):,}"
        )

    with col2:
        st.metric(
            "🏙️ Cities",
            df["City"].nunique()
        )

    with col3:
        st.metric(
            "📍 Localities",
            df["Locality"].nunique()
        )

    with col4:
        st.metric(
            "🏡 Property Types",
            df["Property_Type"].nunique()
        )

    st.markdown("---")

    # =====================================================
    # PRICE INTELLIGENCE
    # =====================================================

    st.subheader("💰 Price Intelligence")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Lowest Property Price",
            f"₹ {df['Price_INR'].min():,.0f}"
        )

    with col2:
        st.metric(
            "Average Property Price",
            f"₹ {df['Price_INR'].mean():,.0f}"
        )

    with col3:
        st.metric(
            "Highest Property Price",
            f"₹ {df['Price_INR'].max():,.0f}"
        )

    st.markdown("---")

    # =====================================================
    # BEST VALUE CITIES
    # =====================================================

    st.markdown("## 🏆 Best Value Cities")

    st.markdown(
        "Cities with the lowest average price per square foot — "
        "where your money goes further."
    )

    city_value = df.copy()

    city_value["Price_per_sqft"] = (
        city_value["Price_INR"] /
        city_value["Area_sqft"]
    )

    city_value = city_value[
        (city_value["Price_INR"] > 0) &
        (city_value["Area_sqft"] > 0) &
        (city_value["Price_per_sqft"] > 0)
    ]

    city_summary = (
        city_value
        .groupby("City")
        .agg(
            Avg_Price_Per_Sqft=("Price_per_sqft", "mean"),
            Avg_Price=("Price_INR", "mean"),
            Avg_Area=("Area_sqft", "mean")
        )
        .sort_values("Avg_Price_Per_Sqft")
        .head(5)
        .reset_index()
    )

    medals = ["🥇", "🥈", "🥉", "🏅", "🏅"]

    cols = st.columns(5)

    for i, row in city_summary.iterrows():

        with cols[i]:

            value_card_html = (
                '<div class="value-card">'
                f'<div class="value-medal">{medals[i]}</div>'
                f'<div class="value-city">{row["City"]}</div>'
                f'<div class="value-price">'
                f'₹{row["Avg_Price_Per_Sqft"]:,.0f}/sqft</div>'
                '</div>'
            )

            st.markdown(value_card_html, unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # BUDGET EXPLORER
    # =====================================================

    st.markdown("## 🎯 Budget Explorer")

    st.write(
        "Select your budget range to discover properties "
        "available across all cities."
    )

    budget_data = df[
        [
            "City",
            "Locality",
            "BHK",
            "Area_sqft",
            "Bathrooms",
            "Property_Type",
            "Price_INR"
        ]
    ].copy()

    budget_data = budget_data.dropna(
        subset=[
            "City",
            "Area_sqft",
            "Price_INR"
        ]
    )

    budget_data = budget_data[
        (budget_data["Price_INR"] > 0) &
        (budget_data["Area_sqft"] > 0)
    ]

    budget_min = int(
        budget_data["Price_INR"].min()
    )

    budget_max = int(
        budget_data["Price_INR"].max()
    )

    selected_budget = st.slider(
        "💰 Your budget range (₹)",
        min_value=budget_min,
        max_value=budget_max,
        value=(budget_min, budget_max),
        step=100000,
        format="₹ %d"
    )

    selected_min, selected_max = selected_budget

    matching_properties = budget_data[
        (budget_data["Price_INR"] >= selected_min) &
        (budget_data["Price_INR"] <= selected_max)
    ].copy()

    if len(matching_properties) > 0:

        matching_count = len(matching_properties)

        average_area = (
            matching_properties["Area_sqft"].mean()
        )

        top_city = (
            matching_properties["City"]
            .value_counts()
            .index[0]
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            listings_card_html = (
                '<div class="budget-card">'
                '<div class="budget-card-title">🏠 Matching Listings</div>'
                f'<div class="budget-card-value">{matching_count:,}</div>'
                '<div class="budget-card-subtitle">'
                'Properties within your budget</div>'
                '</div>'
            )

            st.markdown(listings_card_html, unsafe_allow_html=True)

        with col2:

            area_card_html = (
                '<div class="budget-card">'
                '<div class="budget-card-title">📐 Average Area</div>'
                f'<div class="budget-card-value">{average_area:,.0f} sqft</div>'
                '<div class="budget-card-subtitle">'
                'Average property size</div>'
                '</div>'
            )

            st.markdown(area_card_html, unsafe_allow_html=True)

        with col3:

            top_city_card_html = (
                '<div class="budget-card">'
                '<div class="budget-card-title">🏙️ Top City</div>'
                f'<div class="budget-card-value">{top_city}</div>'
                '<div class="budget-card-subtitle">'
                'Most listings in this budget</div>'
                '</div>'
            )

            st.markdown(top_city_card_html, unsafe_allow_html=True)

        # -------------------------------------------------
        # CITY BREAKDOWN
        # -------------------------------------------------

        st.subheader("🏙️ Cities Within Your Budget")

        city_breakdown = (
            matching_properties
            .groupby("City")
            .agg(
                Listings=("Price_INR", "count"),
                Average_Price=("Price_INR", "mean"),
                Average_Area=("Area_sqft", "mean")
            )
            .sort_values(
                "Listings",
                ascending=False
            )
            .reset_index()
        )

        city_breakdown["Average_Price"] = (
            city_breakdown["Average_Price"]
            .round(0)
            .astype(int)
        )

        city_breakdown["Average_Area"] = (
            city_breakdown["Average_Area"]
            .round(0)
            .astype(int)
        )

        city_breakdown.columns = [
            "City",
            "Listings",
            "Average Price (₹)",
            "Average Area (sqft)"
        ]

        st.dataframe(
            city_breakdown,
            use_container_width=True,
            hide_index=True
        )

        # -------------------------------------------------
        # PROPERTIES WITHIN BUDGET
        # -------------------------------------------------

        st.subheader("🏡 Properties Within Your Budget")

        budget_display = (
            matching_properties[
                [
                    "City",
                    "Locality",
                    "BHK",
                    "Area_sqft",
                    "Bathrooms",
                    "Property_Type",
                    "Price_INR"
                ]
            ]
            .sort_values("Price_INR")
            .head(10)
            .copy()
        )

        budget_display["Price_INR"] = (
            budget_display["Price_INR"]
            .apply(
                lambda x: f"₹ {x:,.0f}"
            )
        )

        st.dataframe(
            budget_display,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "😕 No properties found within this budget range."
        )

        st.info(
            "Try increasing the budget range."
        )


# =========================================================
# TAB 3: MODEL PERFORMANCE
# =========================================================

with tab3:

    st.title("🤖 Machine Learning Performance")

    st.write(
        "Comparison of regression algorithms used "
        "for house price prediction."
    )

    # =====================================================
    # BEST MODEL
    # =====================================================

    st.subheader("🏆 Best Model")

    st.success(
        "🌲 Random Forest Regressor"
    )

    st.write(
        "Random Forest achieved the highest R² score "
        "among the evaluated models."
    )

    # =====================================================
    # RANDOM FOREST PERFORMANCE
    # =====================================================

    st.subheader("📈 Random Forest Performance")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "R² Score",
            "0.98"
        )

    with col2:

        st.metric(
            "MAE",
            "₹ 811,828"
        )

    with col3:

        st.metric(
            "RMSE",
            "₹ 1,012,107"
        )

    st.markdown("---")

    # =====================================================
    # MODEL COMPARISON
    # =====================================================

    st.subheader("⚖️ Model Comparison")

    performance = pd.DataFrame({

        "Algorithm": [
            "Random Forest",
            "Linear Regression",
            "Decision Tree",
            "Optimized Decision Tree",
            "KNN",
            "SVR"
        ],

        "R² Score": [
            0.98,
            0.95,
            0.92,
            0.95,
            0.35,
            -0.02
        ]

    })

    st.dataframe(
        performance,
        use_container_width=True,
        hide_index=True
    )

    # =====================================================
    # WHY RANDOM FOREST
    # =====================================================

    st.markdown("---")

    st.subheader("🌲 Why Random Forest?")

    st.write(
        "• Combines multiple decision trees to produce "
        "more stable predictions."
    )

    st.write(
        "• Captures nonlinear relationships between "
        "property characteristics and house prices."
    )

    st.write(
        "• Achieved the highest R² score among the "
        "tested regression models."
    )

    # =====================================================
    # ENGINEERED FEATURES
    # =====================================================

    st.markdown("---")

    st.subheader("🧠 Engineered Features")

    st.info(
        "The model uses engineered features to provide "
        "additional information about the property."
    )

    st.write("• Bath_BHK_Ratio")
    st.write("• Total_Facilities")
    st.write("• Location_Score")


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "🏠 PropValue AI • "
    "AI-Powered Property Price Prediction"
)
