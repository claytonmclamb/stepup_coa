output$alltime_grid_ui <- renderUI({
  if (clicks_1$n == 0) {
    clicks_1$n <- 1
    actionButton("at_grid_button", label = "Reveal Donors")
  } else {
    HTML('<button id="at_grid_button" type="button" class="btn btn-default action-button">Reveal artists</button> <div id="alltime_grid_html" class="shiny-html-output"></div>')
  }
})

clicks_1 <- reactiveValues(
  n = 0
)