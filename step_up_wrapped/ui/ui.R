fillPage(
  title = "Your Donor History",
  add_busy_spinner(
    spin = "semipolar",
    color = "#a0bd76",
    margins = c(40, 20),
    height = "5%",
    width = "5%"
  ),
  tags$head(
    tags$style(
      css
    ),
    tags$meta(name = "viewport", content = "width=device-width, initial-scale=1.0")
  ),
  useShinyjs(),
  div(
    id = "fullpage",
    source(file.path("ui", "section1.R"), local = TRUE)$value,
    source(file.path("ui", "section2.R"), local = TRUE)$value,
    source(file.path("ui", "section3.R"), local = TRUE)$value
  ),
  tags$script(
    src = "fullpage.js"
  ),
  tags$script(
    src = "https://isuttell.github.io/sine-waves/javascripts/sine-waves.min.js"
  ),
  tags$script(
    src = "waves.js"
  ),
  tags$script(
    src = "https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.17-beta.0/vue.js"
  ),
  tags$script(
    src = "https://cdnjs.cloudflare.com/ajax/libs/localforage/1.7.3/localforage.min.js"
  ),
  tags$script(
    src = "animate.js"
  )
)
