import requests
import json

def get_user_id_by_screen_name(screen_name):
    """
    Lấy user ID từ screen name (username) sử dụng Twitter GraphQL API
    
    Args:
        screen_name (str): Username của user (ví dụ: "elonmusk", "hyperliquidx")
    
    Returns:
        str: User ID nếu thành công, None nếu thất bại
    """
    
    # URL của API
    base_url = "https://x.com/i/api/graphql/1F38Jtjett-7b8eQKstioA/UserByScreenName"
    
    # Variables cho request
    variables = {
        "screen_name": screen_name
    }
    
    # Features cho request
    features = {
        "responsive_web_grok_bio_auto_translation_is_enabled": False,
        "hidden_profile_subscriptions_enabled": True,
        "payments_enabled": False,
        "profile_label_improvements_pcf_label_in_post_enabled": True,
        "rweb_tipjar_consumption_enabled": True,
        "verified_phone_label_enabled": False,
        "subscriptions_verification_info_is_identity_verified_enabled": True,
        "subscriptions_verification_info_verified_since_enabled": True,
        "highlights_tweets_tab_ui_enabled": True,
        "responsive_web_twitter_article_notes_tab_enabled": True,
        "subscriptions_feature_can_gift_premium": True,
        "creator_subscriptions_tweet_preview_api_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "responsive_web_graphql_timeline_navigation_enabled": True
    }
    
    field_toggles = {
        "withAuxiliaryUserLabels": True
    }
    
    # Query parameters
    params = {
        "variables": json.dumps(variables),
        "features": json.dumps(features),
        "fieldToggles": json.dumps(field_toggles)
    }
    
    # Headers từ request gốc
    headers = {
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "content-type": "application/json",
        "cookie": "g_state={\"i_l\":0}; kdt=g8JunwogB8tZ6DVMw9pMYpRwQgt9tcY7BeNgjH59; ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog=%7B%22distinct_id%22%3A%220197c64d-6c07-74e1-8fd9-0c777cdb0dbf%22%2C%22%24sesid%22%3A%5B1751378662309%2C%220197c64d-6c06-701c-8fd2-5c57ee33750d%22%2C1751378652166%5D%7D; cf_clearance=fWup8Ph7EPizc4JdAXMFyl.idHGQP2kOzjCiZqNQTwc-1751742135-1.2.1.1-JofE_.GGU0DmYs5RzG2Iqi2isTgzXjR_OhxWxVsTFCCQSBsHbIGpoxpDeFA2V49pQet6I3cRRUd3PviZClPevagxSa6L5s7hqEHHdSw6D1jfu1i5bXQKlUYHmGrMgzLna9YOKUcV.cdm9SON6xK0y9wBEXM3UHwSg6fKi_3wa83OVE7CwYXtXQg4NEjDluDpUTYLcguI86SHmQ28vQ80W5ix9UHWguKdn66Y1j1zMRk; first_ref=https%3A%2F%2Fwww.vibes.fun%2F; personalization_id=\"v1_0SlALNr/Koa5V415fO48Kg==\"; ads_prefs=\"HBERAAA=\"; auth_multi=\"1888900168076177408:a7c3c9b8c297fa325f8ea09bf331e39a3fa4c664|1907319925712257024:2a8ebf20c70b0042f1fb3e56fb638e4b606771e1|1907081230149136384:7a261a491e879d1f14c6fc346f8e1299d21a2e11|1925110008699559936:7b2b73b83a5d316aa600bb4ed12a128305c5edc3\"; auth_token=352213c27005b45d62bd27adfb88c07d9e1701ce; guest_id_ads=v1%3A175244158426840101; guest_id_marketing=v1%3A175244158426840101; guest_id=v1%3A175244158426840101; twid=u%3D732733835775905792; ct0=fe518dc961f5ac61d3cb3709b7d817e94f9b1c7a2fe69a2275f201d919534018c089fa16bf4ffbbf294bd04e250ecde155b752d47882b817e4be5cc962d5cb39ad312fe8f990fb42b6248244a5d3ee08; lang=en; __cf_bm=vtS4.PeGjAOKef4JnhV5U3szPJkgN2mvT2v6CwEtws0-1752577854-1.0.1.1-dxTxSbYEdGMl2j3CnijVtMcGONW0itn24wS8SYQ6uyVRcd74CXIF7Cl6ElwpSlosLylxRgJ4BYefBXNckjs8dJVLtoVtwXlt03MRseTIxDI",
        "priority": "u=1, i",
        "referer": f"https://x.com/{screen_name}",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-arch": "\"x86\"",
        "sec-ch-ua-bitness": "\"64\"",
        "sec-ch-ua-full-version": "\"138.0.7204.101\"",
        "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"138.0.7204.101\", \"Google Chrome\";v=\"138.0.7204.101\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": "\"\"",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-ch-ua-platform-version": "\"19.0.0\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "x-client-transaction-id": "RRRd+lOtF7xV6jAbmkaUQFI6uDU2XrqHbL93prUAfIbgnL6H054K9+zRjM565LhTW22QY0GIomO/a/TQ+ksj0xoaCVwaRg",
        "x-csrf-token": "fe518dc961f5ac61d3cb3709b7d817e94f9b1c7a2fe69a2275f201d919534018c089fa16bf4ffbbf294bd04e250ecde155b752d47882b817e4be5cc962d5cb39ad312fe8f990fb42b6248244a5d3ee08",
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en",
        "x-xp-forwarded-for": "ca957d27cffa4db894249b869df0e8408b2ee3d75dff2c13f90695e919d87e424a6fe3bb20ce361401f59555eee407147be2363cfe854527b66bef473c775e048029441515cc26daa11309c8738e85fabdb13010cc2b68e6776d974b5b7dccf845f278ae955dadd8784c0118114417b3bb841edb5987477b64aa5b2cf5744ccb86090ce92c1698dcc5dd8410a10d7293e3ddcf8646bf4cfa4ea59c033af78213c3a4c253d53a537731ca1f303245d21eb8675b7404b652b94a8894d81b65d25b8b583feab37a5277face241b5d96c0e27d1311d3e6185d0c5f2295d43d092e16177d1080cd46cbca4be5815930cdaa59b7a02d25f78fc9fc619426"
    }
    
    try:
        # Thực hiện GET request
        response = requests.get(base_url, params=params, headers=headers)
        
        # Kiểm tra status code
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract user ID từ response
        user_id = data.get("data", {}).get("user", {}).get("result", {}).get("rest_id")
        
        if user_id:
            return user_id
        else:
            print(f"❌ Không tìm thấy user ID cho username: {screen_name}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi thực hiện request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Lỗi khi parse JSON: {e}")
        return None

def get_user_tweets(user_id="1527020295059648513", count=20):
    """
    Lấy tweets của user từ Twitter GraphQL API
    
    Args:
        user_id (str): ID của user cần lấy tweets
        count (int): Số lượng tweets cần lấy
    """
    
    # URL của API
    base_url = "https://x.com/i/api/graphql/4cddsYq56gFfTNDAljwNOw/UserTweets"
    
    # Parameters cho request
    variables = {
        "userId": user_id,
        "count": count,
        "includePromotedContent": True,
        "withQuickPromoteEligibilityTweetFields": True,
        "withVoice": True
    }
    
    features = {
        "rweb_video_screen_enabled": False,
        "payments_enabled": False,
        "profile_label_improvements_pcf_label_in_post_enabled": True,
        "rweb_tipjar_consumption_enabled": True,
        "verified_phone_label_enabled": False,
        "creator_subscriptions_tweet_preview_api_enabled": True,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "premium_content_api_read_enabled": False,
        "communities_web_enable_tweet_community_results_fetch": True,
        "c9s_tweet_anatomy_moderator_badge_enabled": True,
        "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
        "responsive_web_grok_analyze_post_followups_enabled": True,
        "responsive_web_jetfuel_frame": True,
        "responsive_web_grok_share_attachment_enabled": True,
        "articles_preview_enabled": True,
        "responsive_web_edit_tweet_api_enabled": True,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": True,
        "view_counts_everywhere_api_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "responsive_web_twitter_article_tweet_consumption_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "responsive_web_grok_show_grok_translated_post": False,
        "responsive_web_grok_analysis_button_from_backend": True,
        "creator_subscriptions_quote_tweet_preview_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": True,
        "longform_notetweets_rich_text_read_enabled": True,
        "longform_notetweets_inline_media_enabled": True,
        "responsive_web_grok_image_annotation_enabled": True,
        "responsive_web_grok_community_note_auto_translation_is_enabled": False,
        "responsive_web_enhance_cards_enabled": False
    }
    
    field_toggles = {
        "withArticlePlainText": False
    }
    
    # Query parameters
    params = {
        "variables": json.dumps(variables),
        "features": json.dumps(features),
        "fieldToggles": json.dumps(field_toggles)
    }
    
    # Headers từ request gốc
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "content-type": "application/json",
        "cookie": "kdt=4DqleXwSngpkqTTkrK2FGx2gO7zFiGs3QEWOBpBM; personalization_id=\"v1_JueYZaEjz3B719IF6ErgOA==\"; first_ref=https%3A%2F%2Fwww.goblin.meme%2F; ads_prefs=\"HBERAAA=\"; auth_multi=\"1539239215040700417:59ad78d9cb072edeb57217c12739e3475d093adf\"; auth_token=f71201ab5ae1da951375ede9b5669bf741168e40; guest_id_ads=v1%3A175227750184711180; guest_id_marketing=v1%3A175227750184711180; guest_id=v1%3A175227750184711180; twid=u%3D1364277232789643267; ct0=ef600d9ddef4750e6ae5f96fdc40e5a56664bac0de08c4815bfcae85d047738a481a053567a8f8d9e10af7aa50300e78b6f0054da1123665112ebed9586f0edb111475b45bc4e2b68527a0d31570242b; lang=en; external_referer=padhuUp37zhVih0f70OgKgNtWixAgKWHqWfCeOw7I44%3D|0|8e8t2xd8A2w%3D; ok_global={\"_expire\":{}}; ok_default={\"_expire\":{}}; ok_okg={\"_expire\":{},\"currentMedia\":\"xl\"}; __cf_bm=_wWauMkEB3A2oG9.X.uwZV4CPTkoPeQtgz0mhl8H9Vs-1752576268-1.0.1.1-XddK_eeK8Y7RUvZiOhpvJNjsEZpUxzFNJGrCxocF6ud7JzN.YfYHoJvaGlgmxwSHnJA_AN_3_FLWrHxpFwl2WiwMlmbPF0t4bT7HQdDeDOM",
        "priority": "u=1, i",
        "referer": "https://x.com/elonmusk",
        "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "x-client-transaction-id": "69hORR1tI4zZ2m0h+MIlpvSTHj+nEO3VB0eJJCM4Q+lYWOyH960nWZbKa9hMz9XZfmQ7ze8nGq+ymNuf2UvRiSUFEunk6A",
        "x-csrf-token": "ef600d9ddef4750e6ae5f96fdc40e5a56664bac0de08c4815bfcae85d047738a481a053567a8f8d9e10af7aa50300e78b6f0054da1123665112ebed9586f0edb111475b45bc4e2b68527a0d31570242b",
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en",
        "x-xp-forwarded-for": "bf1cded312cd6a2579c36151453b9fc51d42c8c6a89dfccda48232add66b829f1eba6fcb6a92b352387ac9f71b72808b074b7137ba5e191d612f38d7f28ef7b5edf218783ec86030d3f43ac698ffd0ec298d524f81f9a34b31e0a46de60a2a23b285467f1fe8611c1e611640dbbce04c42efe6c9862d127085efa09bfbb0f723105a128dd59832c4f9dd72dbb793fc41388fccfa5bdb853c6778cf13175dce0e89dddfd247dc6203350b9fd9ad27954e247186b5cb530ea3ddc06dd6bc46f42262ef391ca61daba5c1b7d6888feb6a34418d0d2f93cb34036b704b4e6fb226fa58ed93af1f772962089da6001cc405369db1e0406d3654e3dd69c9"
    }
    
    try:
        # Thực hiện GET request
        response = requests.get(base_url, params=params, headers=headers)
        
        # Kiểm tra status code
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi thực hiện request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Lỗi khi parse JSON: {e}")
        return None

def get_tweets_by_username(username, count=20):
    """
    Lấy tweets của user bằng username (screen name)
    
    Args:
        username (str): Username của user (ví dụ: "elonmusk", "hyperliquidx")
        count (int): Số lượng tweets cần lấy
    
    Returns:
        dict: Dữ liệu tweets nếu thành công, None nếu thất bại
    """
    print(f"🔍 Đang tìm user ID cho username: {username}")
    
    # Lấy user ID từ username
    user_id = get_user_id_by_screen_name(username)
    
    if user_id:
        print(f"✅ Tìm thấy user ID: {user_id}")
        print(f"📱 Đang lấy {count} tweets...")
        
        # Lấy tweets bằng user ID
        tweets_data = get_user_tweets(user_id, count)
        
        if tweets_data:
            print("✅ Lấy tweets thành công!")
            return tweets_data
        else:
            print("❌ Không thể lấy tweets")
            return None
    else:
        print(f"❌ Không thể tìm thấy user ID cho username: {username}")
        return None

# Hàm phụ để extract tweets từ response
def extract_tweets(data):
    """
    Extract tweets từ response data của Twitter API
    """
    if not data:
        return []
    
    try:
        # Cấu trúc có thể thay đổi, cần kiểm tra thực tế
        instructions = data.get("data", {}).get("user", {}).get("result", {}).get("timeline_v2", {}).get("timeline", {}).get("instructions", [])
        
        tweets = []
        for instruction in instructions:
            if instruction.get("type") == "TimelineAddEntries":
                entries = instruction.get("entries", [])
                for entry in entries:
                    if "tweet" in entry.get("entryId", ""):
                        content = entry.get("content", {})
                        if "itemContent" in content:
                            tweet_results = content["itemContent"].get("tweet_results", {})
                            if "result" in tweet_results:
                                tweets.append(tweet_results["result"])
        
        return tweets
    except Exception as e:
        print(f"Lỗi khi extract tweets: {e}")
        return []

# Sử dụng function
if __name__ == "__main__":
    print("=== TWITTER TWEETS SCRAPER ===")
    
    # Ví dụ sử dụng với username
    username = "hyperliquidx"  # Có thể thay đổi username ở đây
    count = 20
    
    print(f"🎯 Target: @{username}")
    print(f"📊 Số lượng tweets: {count}")
    print("-" * 50)
    
    # Lấy tweets bằng username
    tweets_data = get_tweets_by_username(username, count)
    
    if tweets_data:
        print(f"Kiểu dữ liệu: {type(tweets_data)}")
        
        # In ra cấu trúc dữ liệu (chỉ keys cấp đầu)
        if isinstance(tweets_data, dict):
            print("Các keys chính:", list(tweets_data.keys()))
            
        # Lưu dữ liệu vào file
        with open("tweets_data.json", "w", encoding="utf-8") as f:
            json.dump(tweets_data, f, ensure_ascii=False, indent=2)
        print("💾 Đã lưu dữ liệu vào tweets_data.json")
        
        # Thử extract tweets
        tweets = extract_tweets(tweets_data)
        print(f"📝 Số tweets đã extract: {len(tweets)}")
        
    else:
        print("❌ Không thể lấy dữ liệu")