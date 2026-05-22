from urllib.parse import urlparse
import re


class FeatureExtraction:

    def __init__(self, url):
        self.url = url

    def getFeaturesList(self):

        features = []

        # 1. Using IP Address
        match = re.search(
            r'(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}'
            r'([01]?\d\d?|2[0-4]\d|25[0-5])',
            self.url
        )

        features.append(-1 if match else 1)

        # 2. URL Length
        features.append(1 if len(self.url) < 54 else -1)

        # 3. Shortening Service
        shortening_services = r"bit\.ly|goo\.gl|tinyurl|ow\.ly|t\.co"

        features.append(
            -1 if re.search(shortening_services, self.url) else 1
        )

        # 4. Having @ Symbol
        features.append(-1 if "@" in self.url else 1)

        # 5. Double Slash Redirecting
        features.append(-1 if self.url.rfind('//') > 6 else 1)

        # 6. Prefix Suffix
        features.append(-1 if '-' in urlparse(self.url).netloc else 1)

        # 7. Sub Domains
        dots = urlparse(self.url).netloc.count('.')

        if dots == 1:
            features.append(1)
        elif dots == 2:
            features.append(0)
        else:
            features.append(-1)

        # 8. HTTPS
        features.append(
            1 if self.url.startswith("https://") else -1
        )

        # 9. Domain Registration Length (Dummy)
        features.append(1)

        # 10. Favicon
        features.append(1)

        # 11. Port
        features.append(1)

        # 12. HTTPS Token
        features.append(
            -1 if 'https' in urlparse(self.url).netloc else 1
        )

        # 13. Request URL
        features.append(1)

        # 14. Anchor URL
        features.append(1)

        # 15. Links in Tags
        features.append(1)

        # 16. SFH
        features.append(1)

        # 17. Submitting to Email
        features.append(1)

        # 18. Abnormal URL
        features.append(1)

        # 19. Redirect
        features.append(1)

        # 20. on_mouseover
        features.append(1)

        # 21. RightClick
        features.append(1)

        # 22. Popup Window
        features.append(1)

        # 23. Iframe
        features.append(1)

        # 24. Age of Domain
        features.append(1)

        # 25. DNS Record
        features.append(1)

        # 26. Web Traffic
        features.append(1)

        # 27. Page Rank
        features.append(1)

        # 28. Google Index
        features.append(1)

        # 29. Links Pointing To Page
        features.append(1)

        # 30. Statistical Report
        features.append(1)

        return features