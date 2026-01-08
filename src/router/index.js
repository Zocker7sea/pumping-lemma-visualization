import { createRouter, createWebHistory } from "vue-router"

// Views
import HomeView from "@/components/HomeView.vue"
import PumpingView from "@/components/PumpingView.vue" 

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView
  },
  {
    path: "/languages",
    name: "game",
    component: PumpingView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
