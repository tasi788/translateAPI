var vm = new Vue({
  el: "#app",
  data: {
    input: "",
    resp: [{
      "provider": "google",
      "status": true,
      "result": "文字"
    }]
  },
  methods: {
    async query() {
      this.resp = (await axios.post('/', {
        InputText: this.input
      })).data
    }
  },
});