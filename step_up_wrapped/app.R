library(dotenv)
library(dplyr)
library(highcharter)
#library(httr)
library(lubridate)
library(mlr)
library(plyr)
library(rlist)
library(shiny)
library(shinybusy)
library(shinyjs)
library(shinyWidgets)
library(spotifyr)
library(sass)
library(stringr)
library(waiter)
local <- TRUE
library(shiny)

css <- sass(sass_file("www/styles.scss"))

ui <- source(file.path("ui", "ui.R"), local = TRUE)$value

server <- server <- function(input, output, session) {
  #source(file.path("server", "functions.R"), local = TRUE)$value
  #source(file.path("server", "create_spotify_thingys.R"), local = TRUE)$value
  source(file.path("server", "ui_outputs.R"), local = TRUE)$value
}

shinyApp(ui = ui, server = server)
