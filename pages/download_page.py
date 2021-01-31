class DownloadPage():

    # Page selectors
    PREVIOUS_RELEASES_BUTTON_XPATH = "//p[contains(@onclick,'showPreviousReleases()')]"
    RELEASES_CONTAINER_XPATH = "//*[@id='releasesContainer']"
    EXPAND_BUTTON_XPATH = '//*[@id="3.10-expand"]/img'
    EXPAND_DIV_XPATH = '//*[@id="3.10-expand"]'
    COLLAPSE_DIV_XPATH = '//*[@id="3.10-collapse"]'
    RELEASE_DATA_DIV_XPATH = '//*[@id="3.10-data"]'
    DOWNLOAD_PAGE_URL = "https://www.selenium.dev/downloads/"
    DOWNLOAD_LINK_XPATH = '//a[text()="IEDriverServer_Win32_3.10.0.zip"]'
