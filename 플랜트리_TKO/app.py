import streamlit as st
from datetime import datetime

# --- 1. 페이지 기본 설정 ---
st.set_page_config(page_title="PlanTree - TOKYO", page_icon="✈️", layout="centered")

# --- 2. 약간의 커스텀 CSS (다크모드 최적화) ---
st.markdown("""
<style>
    .title-font { font-size: 28px !important; font-weight: 900; letter-spacing: -1px; }
    .ticket-box { background-color: #1E293B; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid skyblue; }
    .ticket-label { color: skyblue; font-size: 11px; letter-spacing: 1px; }
    .ticket-value { color: white; font-size: 18px; font-weight: bold; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

# --- 3. 헤더 & D-Day 타이머 ---
st.markdown('<p class="title-font">TOKYO <span style="color:skyblue;">PLANTREE</span> ✈️</p>', unsafe_allow_html=True)

target_date = datetime(2026, 4, 27, 9, 45)
now = datetime.now()
d_day = (target_date - now).days

if d_day > 0:
    st.info(f"🚀 출국까지 **D-{d_day}**")
else:
    st.success("🎉 D-DAY!.")

st.divider()

# --- 5. Itinerary (일자별 탭) ---
st.subheader("📅🌳 플랜트리")
tab1, tab2, tab3, tab4 = st.tabs(["4/27(월)", "4/28(화)", "4/29(수)", "4/30(목)"])

with tab1:
    st.markdown("##### ✈️ 도쿄 입성 & 요코하마")
    st.markdown("**09:45** 인천 → 나리타 (제주항공 7C1175)")
    st.markdown("**13:30** 🚆 스카이라이너 (나리타 → 우에노)")
    st.markdown("**16:00** 🚢 요코하마 힐링 투어")
    st.caption("JR 우에노도쿄라인 탑승. 오산바시 국제 여객선 터미널 야경 감상")
    st.link_button("🗺️ 오산바시 터미널 지도", "https://maps.google.com/?q=Osanbashi+Pier")

with tab2:
    st.markdown("##### 🎸 취미 & 👕 패션 다이브")
    st.markdown("**10:00** 오차노미즈 & 아키하바라")
    st.caption("악기 거리(서포팅 타악기/말렛) 및 게임기 구경")
    st.markdown("**14:00** 시부야 & 하라주쿠")
    st.caption("스톤 아일랜드, C.P. 컴퍼니, 울트라스 캐주얼 패션 투어")
    st.link_button("🗺️ 스톤 아일랜드 도쿄", "https://maps.google.com/?q=Stone+Island+Tokyo")

with tab3:
    st.markdown("##### ⚽ MATCH DAY")
    st.markdown("**10:00** 🏟️ 사이타마 스타디움 이동")
    st.caption("JR 우쓰노미야선 -> 셔틀버스. 일찍 도착해서 J리그 서포팅 문화 예습")
    st.error("**15:00 우라와 레즈 vs 가와사키 프론탈레** (홈 자유석)")
    st.link_button("🗺️ 사이타마 스타디움 지도", "https://maps.google.com/?q=Saitama+Stadium+2002")

with tab4:
    st.markdown("##### 🛫 비행의 꿈 & 귀국")
    st.markdown("**13:00** ✈️ 항공 과학 박물관")
    st.caption("조종사 지망생 필수 코스! 747 단면 및 시뮬레이터 체험")
    st.markdown("**18:30** 나리타 → 인천 (제주항공 7C1108)")
    st.link_button("🗺️ 박물관 지도", "https://maps.google.com/?q=Museum+of+Aeronautical+Sciences")

st.divider()

# --- 4. Mission Critical (티켓 & 지도) ---
st.subheader("🚨 MEMO")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="ticket-box">
            <div class="ticket-label">URAWA TICKET</div>
            <div class="ticket-value">2450-5862-77262</div>
        </div>
    """, unsafe_allow_html=True)
    
with col2:
    st.markdown("""
        <div class="ticket-box">
            <div class="ticket-label">HOTEL MAP</div>
            <div class="ticket-value">소테츠 프레사 인 우에노 오카치마치</div>
            <div class="ticket-value">〒110-0005 Tokyo, Taito City, Ueno, 1 Chome−20−8</div>
        </div>
    """, unsafe_allow_html=True)
    st.link_button("📍 구글맵 열기", "https://maps.google.com/?q=소테츠+프레사+인+우에노+오카치마치", use_container_width=True)

st.divider()

# --- 6. Checklists ---
col_chk1, col_chk2 = st.columns(2)
with col_chk1:
    st.subheader("✅ 행정 & 서류")
    st.checkbox("우라와 티켓 예매", value=True)
    st.checkbox("Payments 준비")
    st.checkbox("eSIM 준비")
    

with col_chk2:
    st.subheader("🎒 핵심 준비물")
    st.checkbox("트래블로그 카드")
    st.checkbox("여권")
    st.checkbox("110V 돼지코")
