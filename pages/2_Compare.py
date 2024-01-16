import streamlit as st
import pandas as pd

st.title('Selected Left Back Comparison')
st.image('Plots/compare.png', use_column_width=True)
st.subheader('Variable Description')




data = {
    'Variable': ['turnovers_90', 'fouls_90', 'minutes', 'pressures_90','padj_pressures_90','box_cross_ratio','obv_pass_90','op_passes_into_box_90',
                 'pressure_regains_90','padj_tackles_and_interceptions_90','obv_defensive_action_90','aerial_ratio','deep_progressions_90','obv_dribble_carry_90'],
    'Description': ['Number of lost balls per game', 'Fouls committed per game', 'Minutes platyed', 'The number of times a player pressures an opposition player per game',
                    'Number of times a player pressures an opposition player proportional to teams posession', 'Successful crosses into box per game', 'Average passing quality/value per 90',
                    'Passes into oppostion box from open play per game','Number of balls won via pressures per game', 'Number of tackles and postions won adjusted for team posession per game',
                    'Average defensive action quality/value per game', 'Percentage of balls won in the air', 'Balls moved from own half far up the pitch per game','Average dribbling quality/value per game' ]
}
df = pd.DataFrame(data)

st.table(df)